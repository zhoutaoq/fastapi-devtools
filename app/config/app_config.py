from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class AppConfigSettings(BaseSettings):
    """应用配置"""
    app_name: str = ""
    app_port: int
    app_env: str = "dev"
    app_debug: bool = False
    """jwt配置"""
    jwt_enable: bool = False
    jwt_secret_key: str = "12345789@98765431"
    jwt_algorithm: str = "HS256"
    jwt_expired: int = 30
    jwt_iss: str
    jwt_no_check_uris: str
    """数据库配置"""
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str
    """redis配置"""
    redis_dsn: RedisDsn = None
