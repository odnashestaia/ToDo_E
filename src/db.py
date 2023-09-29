from typing import AsyncGenerator


from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

from src.config import DB_HOST, DB_PASS, DB_USER, DB_PORT, DB_NAME


""" DATABASE_URL ссылка на базу данных в начале название бд+драйвер который используется для работы с бд (в нашем случае асинхронный)"""
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


metadata = MetaData()


class Base(DeclarativeBase):
    pass


""" точка входа SQLAlchemy (то есть соединения) """
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """ получаем ссесию """
    async with async_session_maker() as session:
        yield session
