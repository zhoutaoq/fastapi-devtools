import logging

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.middleware.jwt_token import JwtManageUtil, secret_key
from app.models.response import response

# 不检查
check_token_path_list = [
    "/v1/user/user/token",
]


class JwtMiddleware(BaseHTTPMiddleware):
    """ jwt验证中间件 """

    def __init__(self, app):
        super().__init__(app)
        self.jwtUtil = JwtManageUtil(secret=secret_key)

    async def dispatch(self, request: Request, call_next):
        # 判断路由是否需要验证
        path = request.url.path
        logging.info(f"dispatch path :{path}")
        if path not in check_token_path_list:
            return await call_next(request)
        # 获取token
        token = request.headers.get('x-token', '')
        if token == "":
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response.ResponseFail('token不能为空~')))

        # 验证token
        tokenInfo = self.jwtUtil.decode(token)
        if not tokenInfo:
            # 验证失败
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response.ResponseFail(f"无效的 token: ['{token}']")))

        result = await call_next(request)
        print("token解析成功", tokenInfo)
        return result
