from fastapi import FastAPI
from data_calls import five_year_treasury, prime_rate, dow, dow_price_change
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Rates(BaseModel):
    id: int
    rate: float

db: List[Rates] = [
    Rates(
        id = 1,
        rate = five_year_treasury()
    ),
    Rates(
        id = 2,
        rate = prime_rate()
    ),
    Rates(
        id = 3,
        rate = dow()
    ),
    Rates(
        id = 4,
        rate = dow_price_change()
    )
]

@app.get("/rates")
async def fetch_all_rates():
    return db

@app.get("/rates/{id}")
def treasury(id: int):
    return {"rate": db[(id-1)]}

