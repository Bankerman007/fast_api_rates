from fastapi import FastAPI
from data_calls import five_year_treasury, prime_rate, dow, dow_price_change
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Rates(BaseModel):
    id: int
    rate: float
    
five_year_treasury = five_year_treasury()
prime = prime_rate()
dow = dow()
dow_price_change = dow_price_change()

db: List[Rates] = [
    Rates(
        id = 1,
        rate = five_year_treasury
    ),
    Rates(
        id = 2,
        rate = prime
    ),
    Rates(
        id = 3,
        rate = dow
    ),
    Rates(
        id = 4,
        rate = dow_price_change
    )
]


@app.get("/rates")
async def fetch_all_rates():
    return db

@app.get("/rates/{id}")
def treasury(id: int):
    return {"rate": db[(id-1)]}



