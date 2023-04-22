from sqlalchemy import select

from app.database import async_session_maker


class BaseCrud:
    model = None

    @classmethod
    async def get_one_by_id(cls, pk):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=pk)
            return (await session.execute(query)).scalar_one_or_none()

    @classmethod
    async def get_one_or_none(cls, **filter_args):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_args)
            return (await session.execute(query)).scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_args):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_args)
            return (await session.execute(query)).scalars().all()
