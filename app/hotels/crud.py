from app.base.base_crud import BaseCrud
from app.hotels.models import Booking


class BookingCrud(BaseCrud):
    model = Booking
