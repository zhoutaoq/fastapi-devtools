from fastapi import APIRouter, HTTPException, Body

from app.crud.user.user import UserCRUD
from app.db.postgresql_db import engine, session_maker
from app.models.response import response
from app.models.user.user import User, UserParam
from app.schemas.user import UserProfileSchema

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


@user_router.get("/user/token", summary="token样例")
async def token_sample(param: str):
    return response.ResponseSuccess(param)


# 创建异步session
async_session = session_maker(engine)
mapper = UserCRUD(User)


@user_router.post("/user/create", summary="create user")
async def create_user(user: User):
    user = await mapper.create_user(async_session, user)
    return user


@user_router.post("/user/query", summary="query user")
async def query_user(user: User):
    user = await mapper.get_by_username(async_session, user.username)
    return user


@user_router.post("/user/update", summary="update user")
async def update_user(user: User):
    user = await mapper.update(async_session, user.id, user.dict())
    return user


@user_router.post("/user/delete", summary="delete user")
async def delete_user(user: User):
    result = await mapper.delete(async_session, user.id)
    return response.ResponseSuccess(result)


@user_router.post("/user/info/query", summary="query user with profile")
async def query_user_with_profile(id: str):
    user_info_data = await mapper.get_user_with_profile(async_session, id)
    return response.ResponseSuccess(user_info_data)


@user_router.post("/user/profile/query", summary="query user and profile")
async def query_user_profile(id: str):
    user_data = await mapper.get_by_user_id(async_session, id)
    user_profile_data = await mapper.get_user_profile(async_session, id)
    return response.ResponseSuccess({"user": user_data, "profile": user_profile_data})


@user_router.post("/user/profile/update", summary="update user profile")
async def update_user_profile(user_model: UserProfileSchema = Body(...), ):
    profile_update_data = user_model.dict(
        include={"nickname", "avatar_url", "birth_date", "bio"}, exclude_unset=True)
    await mapper.update_user_profile(async_session, user_model.user_id, profile_update_data)
    return response.ResponseSuccess(profile_update_data)
