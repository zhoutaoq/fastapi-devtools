#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from fastapi import APIRouter
from app.api.v1.endpoints.system.system import system_router
from app.api.v1.endpoints.user.user import user_router

# 创建v1版本的路由
v1_router = APIRouter(prefix="/v1")

# 注册到v1_router中
v1_router.include_router(system_router)
v1_router.include_router(user_router)

