#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from typing import Callable
from fastapi import FastAPI
from app.core.custom_logger import logger




def startup(app: FastAPI) -> Callable:
    async def app_startup() -> None:
        logger.info("项目开始运行...")

    return app_startup


def shutdown(app: FastAPI) -> Callable:
    async def app_shutdown() -> None:
        logger.info("项目停止运行...")

    return app_shutdown
