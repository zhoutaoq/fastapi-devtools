from datetime import date
from typing import Optional

from sqlmodel import Field

from app.models.base_model import Base


class UserProfile(Base, table=True):
    """ 用户资料模型 """
    __tablename__ = "users_profiles"

    user_id: str = Field(description="关联的用户ID", foreign_key="users.id")
    avatar_url: Optional[str] = Field(description="用户头像URL")
    nickname: Optional[str] = Field(max_length=50, description="用户昵称")
    birth_date: Optional[date] = Field(default=None, description="出生日期-")
    bio: Optional[str] = Field(max_length=255, description="用户简介_")
