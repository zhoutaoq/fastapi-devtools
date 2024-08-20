from datetime import datetime
from typing import Optional,Any

from pydantic import BaseModel, Field


class HttpResponse(BaseModel):
    """http统一响应"""
    code: int = Field(default=200)  # 响应码
    msg: str = Field(default="successful")  # 响应信息
    data: Optional[Any] = None  # 具体数据


def ResponseSuccess(resp: Any) -> HttpResponse:
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(code=200, msg=f"{currentTime} 成功", data=resp)


def ResponseFail(msg: str, code: int = -1) -> HttpResponse:
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(
        code=code, msg=f"{currentTime} 失败", data=msg)
