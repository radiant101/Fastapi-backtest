from pydantic import BaseModel,condecimal,Field
from datetime import datetime
from decimal import Decimal


class StockPriceInput(BaseModel):
    datetime: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int

class StockPriceOutput(StockPriceInput):
    id: int  # Auto-generated primary key

    class Config:
        from_attributes = True  # Allows ORM compatibility
