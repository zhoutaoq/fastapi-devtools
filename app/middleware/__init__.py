from fastapi import FastAPI

from .usetime_middleware import UseTimeMiddleware
from .jwt_middleware import JwtMiddleware


def registerMiddlewareHandle(server: FastAPI):
    # 添加耗时请求中间件
    server.add_middleware(UseTimeMiddleware)
    # server.add_middleware(JwtMiddleware)
