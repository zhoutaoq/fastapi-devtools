from fastapi import FastAPI

from .usetime_middleware import UseTimeMiddleware


def registerMiddlewareHandle(server: FastAPI):
    # 添加耗时请求中间件
    server.add_middleware(UseTimeMiddleware)
