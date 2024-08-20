from fastapi import Request
from app.core.custom_logger import logger
import time


async def log_middleware(request: Request, call_next):
    # 记录请求的方法、URL和处理时间
    start_time = time.time()
    # 调用下一个中间件
    response = await call_next(request)
    # 计算处理时间
    process_time = time.time() - start_time
    # 记录日志
    log_dict = {
        "method": request.method,
        "url": request.url,
        "process_time": process_time
    }
    logger.info(log_dict, extra=log_dict)

    return response
