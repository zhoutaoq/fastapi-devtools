from fastapi import APIRouter, HTTPException

from app.models.response import response
from app.models.user.user import User, UserParam

user_router = APIRouter(prefix="/user", tags=["用户接口"])

user_router.get("/user/params")

DIC = {"a": "a1", "c": "c2", "d": "d3"}


@user_router.get("/user/params", summary="获取用户参数")
async def get_user_params(params_name: str):
    if not params_name or params_name not in DIC:
        raise HTTPException(status_code=404, detail=f"参数 {params_name} 未找到。")
    return DIC[params_name]


@user_router.post("/user/params", summary="新增用户参数")
async def add_user_params(user_params: str):
    DIC[user_params] = user_params + "9"
    return DIC


@user_router.post("/user/post", summary="用户post请求")
async def add_user_params(user_data: User):
    print(f'接收到：{user_data}')
    return user_data


@user_router.post("/user/valid", summary="参数校验样例")
async def params_valid_sample(user_data: UserParam):
    print(f'接收到：{user_data}')
    return user_data


@user_router.post("/user/result", summary="返回参数样例")
async def params_valid_sample(param: str):
    forbidden = ['A', 'B', 'C', 'D']
    if param in forbidden:
        return response.ResponseFail(f"参数 {forbidden} 不被允许~")
    return response.ResponseSuccess(param)
