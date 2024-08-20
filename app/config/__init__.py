from dotenv import load_dotenv
from .app_config import *

# 加载 .env 文件
load_dotenv()
# 实例化配置模型
appSettings = AppConfigSettings()