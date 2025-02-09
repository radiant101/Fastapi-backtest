from fastapi import APIRouter,HTTPException
from app.database import prisma
from app.schemas import StockPriceInput, StockPriceOutput 
from typing import List

router=APIRouter() 

@router.get("/data", response_model=List[StockPriceOutput])  #get request
async def get_data():
    records=await prisma.stockprice.find_many()  #fetching stock
    return records

@router.post("/data", response_model=StockPriceOutput) #post reqeuest
async def add_data(stock_data: StockPriceInput):
    new_record = await prisma.stockprice.create(data=stock_data.model_dump())  # inserting new record
    return new_record  # return  inserted data