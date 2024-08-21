from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.models.response import response


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_msg = ""
    for error in exc.errors():
        error_msg += ".".join(error.get("loc")) + ":" + error.get("msg") + ";"
    # 这里response.ResponseFail是上篇文章中的内容
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response.ResponseFail(error_msg)))
