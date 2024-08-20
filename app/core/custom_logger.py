# -*- coding: utf-8 -*-

import logging
import sys
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from logtail import LogtailHandler  # 来自这个库logtail-python

# https://logs.betterstack.com/
token = "4iarYB1x2KaWRAhJxNFozWVs"

# create logger
logger = logging.getLogger()
formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s'
)

# 确保/logs目录存在
logs_dir = "./logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
# 设置文件日志处理器，每天生成一个日志文件
today = datetime.today().strftime('%Y-%m-%d')
file_handler = TimedRotatingFileHandler(
    filename=os.path.join(logs_dir, f'{today}.log'),
    when="midnight",
    interval=1,
    encoding='utf-8',
    utc=True,
    backupCount=30  # 可以调整保留日志文件的数量，这里示例为保留最近30天的日志
)
better_stack_handler = LogtailHandler(source_token=token)

# set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 设置文件名扩展，使用日期作为文件名的一部分
file_handler.suffix = "%Y-%m-%d.log"

# add handlers to logger
logger.handlers = [stream_handler, file_handler, better_stack_handler]

# set log level
logger.setLevel(logging.INFO)