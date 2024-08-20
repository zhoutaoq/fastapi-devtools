from fastapi import APIRouter, HTTPException

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
