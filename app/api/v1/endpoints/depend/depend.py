from fastapi import APIRouter, Depends

from app import depends
from app.models.response import response

depends_router = APIRouter(prefix="/ds", tags=["depends_sample"], dependencies=[Depends(depends.verify_token)])


@depends_router.get("/autowired/token")
async def autowired(param: str):
    return response.ResponseSuccess(param)
