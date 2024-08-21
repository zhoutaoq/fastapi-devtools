import logging
from typing import TypeVar, Generic, Type, Optional, List

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from sqlmodel import SQLModel

# Define a generic variable T, which must be a subclass of SQLModel
T = TypeVar('T', bound=SQLModel)


class BaseCRUD(Generic[T]):
    def __init__(self, model: Type[T]):
        """
        初始化时指定CRUD操作的模型类。
        """
        self.model = model

    async def get_all(self, async_session: async_sessionmaker[AsyncSession]) -> List[T]:
        async with async_session() as session:
            statement = select(self.model).order_by(self.model.id)
            result = await session.execute(statement)
            return result.scalars().all()

    async def add(self, async_session: async_sessionmaker[AsyncSession], obj: T) -> T:
        async with async_session() as session:
            session.add(obj)
            await session.commit()
            return obj

    async def get_by_id(self, async_session: async_sessionmaker[AsyncSession], obj_id: str) -> Optional[T]:
        async with async_session() as session:
            statement = select(self.model).filter(self.model.id == obj_id)
            result = await session.execute(statement)
            return result.scalars().first()

    async def update(self, async_session: async_sessionmaker[AsyncSession], obj_id: str, data: dict) -> Optional[T]:
        async with async_session() as session:
            obj = await self.get_by_id(async_session, obj_id)
            if obj:
                # todo this way cant save the entity data to database, need to resolve this problem later
                # for key, value in data.items():
                #     setattr(obj, key, value)
                # print(f"Session dirty before commit: {session.dirty}")
                # await session.commit()
                # print(f"Session dirty after commit: {session.dirty}")
                clazz = type(obj)
                stmt = (
                    update(clazz).
                    where(clazz.id == obj_id).
                    values(**data)
                )
                await session.execute(stmt)
                await session.commit()
                logging.info('update obj is not None')
            else:
                logging.info('update obj is None')
            return obj

    async def delete(self, async_session: async_sessionmaker[AsyncSession], obj_id: str) -> bool:
        async with async_session() as session:
            obj = await self.get_by_id(async_session, obj_id)
            if obj:
                await session.delete(obj)
                await session.commit()
                return True
            return False
