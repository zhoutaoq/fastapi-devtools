from typing import Optional

from pydantic import BaseModel, constr, conint, validator
from sqlalchemy import Integer
from sqlmodel import Field, Column

from app.models.base_model import Base
from app.models.user.user_enum import UserStatus


class User(Base, table=True):
    """ 用户模型 """
    __tablename__ = "users"

    username: Optional[str] = Field(index=True, unique=True, min_length=6, max_length=50, description="用户名")
    hashed_password: Optional[str] = Field(description="哈希密码")
    email: Optional[str] = Field(index=True, unique=True, description="邮箱")
    phone_number: Optional[str] = Field(index=True, min_length=1, max_length=20, description="手机号码")
    status: UserStatus = Field(default=UserStatus.ACTIVE, sa_column=Column(Integer), description="状态")


class UserParam(BaseModel):
    user_name: str  # 基本类型
    age: conint(ge=18, le=30)  # 整数范围：18 <= age <= 30
    # List[constr(min_length=1, max_length=3)] : 限制列表中的每个字符串长度的范围
    address: constr(min_length=6, max_length=10)  # 字符长度

    @validator("user_name")
    def validateUsername(cls, value: str):
        if value.find("傻") > -1:
            raise ValueError("user_name不能包含敏感词")
        return value
