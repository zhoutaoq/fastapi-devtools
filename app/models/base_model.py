from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
import uuid


class Base(SQLModel):
    """基类，包含id、创建日期和更新日期"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, unique=True, index=True,
                    max_length=128, description="ID")
    create_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(), description="创建时间")
    update_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(), description="最后更新时间")
