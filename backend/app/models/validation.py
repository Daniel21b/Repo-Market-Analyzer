from pydantic import BaseModel, Field
from datetime import date

class RepoMarketData(BaseModel):
    start_date: date
    end_date: date
    bank: str
    loan_amount: float

    class Config:
        schema_extra = {
            "example": {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31",
                "bank": "Bank A",
                "loan_amount": 1000000.0
            }
        }
