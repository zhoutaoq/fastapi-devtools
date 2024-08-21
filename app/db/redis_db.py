import os

import aioredis
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")
# Global variables are used to store Redis connection pools
redis_pool = None


async def get_redis_pool():
    global redis_pool
    if redis_pool is None:
        REDIS_URL = os.getenv("REDIS_URL")
        redis_pool = await aioredis.create_redis_pool(REDIS_URL, encoding="utf-8")
    return redis_pool
