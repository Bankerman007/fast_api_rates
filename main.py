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
        rate = 1.00
    ),
    Rates(
        id = 2,
        rate = 1.00
    ),
    Rates(
        id = 3,
        rate = 1.00
    ),
    Rates(
        id = 4,
        rate = 1.00
    )
]


@app.get("/rates")
async def fetch_all_rates():
    db[0].rate = five_year_treasury()
    db[1].rate = prime_rate()
    db[2].rate = dow_price_change()
    db[3].rate = dow()
    return db

@app.get("/rates/{id}")
def treasury(id: int):
    db[0].rate = five_year_treasury()
    db[1].rate = prime_rate()
    db[2].rate = dow_price_change()
    db[3].rate = dow()
    return {"rate": db[(id-1)]}

print(db)