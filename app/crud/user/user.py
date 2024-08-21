from typing import Optional

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlmodel import select

from app.crud.base_crud import BaseCRUD
from app.models.user import User
from app.models.user.user_profile import UserProfile
from app.schemas.user import UserInfoSchema


class UserCRUD(BaseCRUD[User]):
    """ 用户CRUD操作"""

    async def get_by_username(self, async_session: async_sessionmaker[AsyncSession], username: str) -> Optional[User]:
        """ 通过用户名获取用户信息 """
        async with async_session() as session:
            statement = select(self.model).where(self.model.username == username)
            result = await session.execute(statement)
            return result.scalars().first()

    async def get_by_email(self, async_session: async_sessionmaker[AsyncSession], email: str) -> Optional[User]:
        """ 通过邮箱获取用户信息 """
        async with async_session() as session:
            statement = select(self.model).where(self.model.email == email)
            result = await session.execute(statement)
            return result.scalars().first()

    async def get_by_phone_number(self, async_session: async_sessionmaker[AsyncSession], phone_number: str,
                                  country_code: str) -> Optional[User]:
        """ 通过手机号码和国际区号获取用户信息 """
        async with async_session() as session:
            statement = select(self.model).where(self.model.phone_number == phone_number,
                                                 self.model.country_code == country_code)
            result = await session.execute(statement)
            return result.scalars().first()

    async def get_by_user_id(self, async_session: async_sessionmaker[AsyncSession], user_id: str) -> Optional[User]:
        """ 通过用户ID获取用户信息 """
        async with async_session() as session:
            statement = select(self.model).where(self.model.id == user_id)
            result = await session.execute(statement)
            return result.scalars().first()

    async def create_user(self, async_session: async_sessionmaker[AsyncSession], user: User) -> User:
        """ 创建用户 """
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update_user(self, async_session: async_sessionmaker[AsyncSession], user_id: str,
                          update_user: dict) -> User:
        """ 更新用户表的信息 """
        async with async_session() as session:
            statement = select(User).filter(User.id == user_id)
            result = await session.execute(statement)
            user = result.scalars().first()
            for key, value in update_user.items():
                setattr(user, key, value)
            await session.commit()
            return user

    # todo NOTICE: Example of a one-to-many query associated with primary and slave
    async def get_user_with_profile(self, async_session: async_sessionmaker[AsyncSession], user_id: str) -> Optional[
        UserInfoSchema]:
        async with async_session() as session:
            statement = select(self.model).where(self.model.id == user_id)
            result = await session.execute(statement)
            user = result.scalars().first()
            profile_statement = select(UserProfile).where(UserProfile.user_id == user_id)
            profile_result = await session.execute(profile_statement)
            profile_list = profile_result.scalars().all()
            user_info_schema = UserInfoSchema()
            user_info_schema.set_properties(user, profile_list)
            return user_info_schema

    async def get_user_profile(self, async_session: async_sessionmaker[AsyncSession], user_id: str) -> Optional[
        UserProfile]:
        """ 获取用户资料 """
        async with async_session() as session:
            statement = select(UserProfile).where(UserProfile.user_id == user_id)
            result = await session.execute(statement)
            return result.scalars().first()

    async def update_user_profile(self, async_session: async_sessionmaker[AsyncSession], user_id: str,
                                  profile_update: dict):
        """ 更新用户资料表的信息 """
        async with async_session() as session:
            statement = select(UserProfile).filter(UserProfile.user_id == user_id)
            result = await session.execute(statement)
            profile = result.scalars().first()
            if not profile:
                profile = UserProfile(user_id=user_id)
                session.add(profile)
            for key, value in profile_update.items():
                setattr(profile, key, value)
            await session.commit()
            return profile
