from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed, Text

from app.database import Base


class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    image_id = Column(Integer, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotels.id'))
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed('(date_to - date_from) * price'))
    total_days = Column(Integer, Computed('date_to - date_from'))
