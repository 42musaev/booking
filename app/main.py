from fastapi import FastAPI, Depends
from fastapi import Query
from typing import Optional, List
from datetime import date

from pydantic import BaseModel

app = FastAPI()


class Booking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class Hotel(BaseModel):
    address: str
    name: str
    stars: int


class HotelSearchParams:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get('/hotels')
def get_hotels(params: HotelSearchParams = Depends()) -> List[Hotel]:
    hotels = [
        {
            'address': 'Moscow st.Grow 1',
            'name': 'Moscow Hotel 1',
            'stars': 5,
        },
        {
            'address': 'St.Petersburg st.White 1',
            'name': 'Petersburg Hotel 1',
            'stars': 10,
        }
    ]
    return hotels