from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

DB_HOST = '0.0.0.0'
DB_PORT = '5455'
DB_NAME = 'postgres_fastapi'
DB_USER = 'postgres'
DB_PASSWORD = 'password'

DATABASE_URI = settings.get_db_uri

engine = create_async_engine(DATABASE_URI)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
