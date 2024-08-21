import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

load_dotenv()
POSTGRES_URL = os.getenv('POSTGRES_URL')
engine = create_async_engine(url=POSTGRES_URL, echo=True)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


def session_maker(db_engine):
    return async_sessionmaker(bind=db_engine, expire_on_commit=False)
