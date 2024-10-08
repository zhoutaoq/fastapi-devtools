from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app.middleware.log_middleware import log_middleware
from . import middleware
from .api.v1.routes import v1_router
from .core.config import settings
from .core.events import startup, shutdown
from .depends import verify_token
from .errors import register_custom_error_handle


def create_app():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        docs_url="/",
        description=settings.PROJECT_DESC,
        # add this param autowired to the whole app
        dependencies=[Depends(verify_token)]
    )

    # 注册事件
    app.add_event_handler("startup", startup(app))
    app.add_event_handler("shutdown", shutdown(app))
    # app.add_event_handler("startup", lambda: startup(app))
    # app.add_event_handler("shutdown", lambda: shutdown(app))

    # 添加CORS中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:7000", "https://localhost:7000", "http://127.0.0.1:7000"],
        # 允许的源列表，适当调整以匹配你的前端应用地址
        allow_credentials=True,
        allow_methods=["*"],  # 允许所有方法
        allow_headers=["*"],  # 允许所有头部
    )

    # register custom midware
    app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
    middleware.registerMiddlewareHandle(app)

    # register custom error handler
    register_custom_error_handle(app)

    # register v1_router
    app.include_router(v1_router)

    return app
