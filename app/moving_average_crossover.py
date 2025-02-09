from fastapi import APIRouter, HTTPException
from app.database import prisma
import pandas as pd


routers = APIRouter()

def moving_average_crossover(df):
    
    df['sma50'] = df['close'].rolling(window=50).mean()
    df['lma100'] = df['close'].rolling(window=100).mean()
    return df

def generate_signal(df):   #generate signal buy and sell or golden crossover
    df['signal'] = ""      # Initialize an empty column
    
    for i in range(1, len(df)):
        if pd.isna(df.loc[i, 'sma50']) or pd.isna(df.loc[i, 'lma100']):
            continue 
        
        if df.loc[i,'sma50'] >= df.loc[i,'lma100'] and df.loc[i-1,'sma50'] < df.loc[i-1,'lma100']:
            df.loc[i,'signal'] = "buy"

        elif df.loc[i,'sma50'] <= df.loc[i,'lma100'] and df.loc[i-1,'sma50'] > df.loc[i-1,'lma100']:
            df.loc[i,'signal'] = "sell"

    return df

@routers.get("/strategy/performance")
async def get_strategy_performance():
    try:
        # fetched data and converted to dataframe
        data = await prisma.stockprice.find_many()
        df = pd.DataFrame([row.model_dump() for row in data])  

        if df.empty:
            raise HTTPException(status_code=404, detail="No data found.")

        # Convert data types causing errors
        df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
        df['volume'] = df['volume'].astype(int)


        df = moving_average_crossover(df)

        df = generate_signal(df)

        # Counting signals
        total_buys = (df['signal'] == 'buy').sum()
        total_sells = (df['signal'] == 'sell').sum()
        
        return {
       "total_buys": int(total_buys),
       "total_sells": int(total_sells),
        "strategy_data" :df.iloc[49:].astype(str).to_dict(orient="records") 
          # 49 because first 48 will show nan
       }

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
