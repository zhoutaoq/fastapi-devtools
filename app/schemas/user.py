from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreateByEmailSchema(BaseModel):
    """ 通过电子邮件注册用户的Schema """
    email: Optional[EmailStr] = Field(None, description="电子邮件")
    password: Optional[str] = Field(None, min_length=6, max_length=20, description="密码",
                                    json_schema_extra={"example": "yourpassword"})


class RegisterRequest(BaseModel):
    """ 通过用户名注册用户的Schema """
    username: Optional[str] = Field(None, description="用户名", json_schema_extra={"example": "yourusername"})
    password: Optional[str] = Field(None, min_length=6, max_length=20, description="密码",
                                    json_schema_extra={"example": "yourpassword"})


class UserCreateByUsernameSchema(BaseModel):
    """ 通过用户名注册用户的Schema """
    username: Optional[str] = Field(None, description="用户名", json_schema_extra={"example": "yourusername"})
    password: Optional[str] = Field(None, min_length=6, max_length=20, description="密码",
                                    json_schema_extra={"example": "yourpassword"})


class UserCreateByPhoneSchema(BaseModel):
    """ 通过手机号码注册用户的Schema """
    country_code: Optional[str] = Field(None, min_length=1, max_length=4, description="国际区号",
                                        json_schema_extra={"example": "86"})
    phone_number: Optional[str] = Field(None, min_length=1, max_length=20, description="手机号码",
                                        json_schema_extra={"example": "13800138000"})
    password: Optional[str] = Field(None, min_length=6, max_length=20, description="密码",
                                    json_schema_extra={"example": "yourpassword"})
    # 验证码
    sms_code: Optional[str] = Field(None, min_length=6, max_length=6, description="验证码",
                                    json_schema_extra={"example": "123456"})


class TokenResponseSchema(BaseModel):
    """ Token响应Schema """
    access_token: str
    token_type: str
    expires_in: float


class UpdateUserSchema(BaseModel):
    username: Optional[str] = Field(None, min_length=6, max_length=50)
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = Field(None, min_length=1, max_length=20)
