from fastapi import APIRouter, HTTPException, Depends

from app import depends
from app.config import appSettings
from app.models.response import response

system_router = APIRouter(prefix="/system", tags=["系统接口"])

system_router.get("/system/params")

DIC = {"a": "a1", "c": "c2", "d": "d3"}


@system_router.get("/system/params", summary="获取系统参数")
async def get_system_params(params_name: str):
    if not params_name or params_name not in DIC:
        raise HTTPException(status_code=404, detail=f"参数 {params_name} 未找到。")
    return DIC[params_name]


@system_router.post("/system/params", summary="新增系统参数")
async def add_system_params(system_params: str):
    DIC[system_params] = system_params + "9"
    return DIC


@system_router.post("/system/settings", summary="查询系统配置")
async def add_system_params():
    return appSettings


@system_router.get("/system/autowired/method", summary="方法级别依赖注入")
async def depends_autowired_method(
        token: str = Depends(depends.verify_token),
):
    return response.ResponseSuccess(token)
