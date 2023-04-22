from fastapi import FastAPI

from app.hotels.router import bookings

app = FastAPI()

app.include_router(bookings)
