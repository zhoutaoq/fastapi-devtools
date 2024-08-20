from typing import Optional

from sqlmodel import Field

from app.models.base_model import Base


class User(Base, table=True):
    """ 用户模型 """
    __tablename__ = "users"

    username: Optional[str] = Field(index=True, unique=True, min_length=6, max_length=50, description="用户名")
    email: Optional[str] = Field(index=True, unique=True, description="邮箱")
    phone_number: Optional[str] = Field(index=True, min_length=1, max_length=20, description="手机号码")
