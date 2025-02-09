import psycopg2
import pandas as pd
import os

DATABASE_URL = os.getenv("DATABASE_URL")
df=pd.read_excel("HINDALCO_1D.xlsx").drop(columns=['instrument'],errors='ignore')

df = df[['datetime', 'open', 'high', 'low', 'close', 'volume']]
# Convert datetime to datetime object and volume to integer
df['datetime'] = pd.to_datetime(df['datetime'])
df['volume'] = df['volume'].astype(int)

def insert_data():
    conn=psycopg2.connect(DATABASE_URL)
    curr=conn.cursor()
    try:
     for index,row in df.iterrows():
        curr.execute(
            'INSERT INTO "StockPrice" (datetime,open,high,low,close,volume) VALUES (%s, %s, %s, %s, %s, %s)',
             (row['datetime'], row['open'], row['high'], row['low'], row['close'], row['volume'])
        )
    
     conn.commit()  # Save changes
     print("Data Inserted Successfully!")
    except Exception as e:
     print('error caused inserting',e)
     conn.rollback()  # Close after work is done
    finally:
        curr.close()  
        conn.close()  

try:
    insert_data()
except Exception as e:
    print("Script Error:", e)