from typing import List

from fastapi import APIRouter

from app.hotels.crud import BookingCrud
from app.hotels.schemas import SchemaBooking

bookings = APIRouter(prefix='/bookings', tags=['bookings'])


@bookings.get('')
async def get_bookings() -> List[SchemaBooking]:
    return await BookingCrud.get_all()


@bookings.get('/{booking_id}')
async def get_booking(booking_id: int) -> SchemaBooking:
    return await BookingCrud.get_one_by_id(booking_id)
