class Settings():
    # 项目名称
    PROJECT_NAME: str = "fastapi-devtools"
    # 项目版本
    PROJECT_VERSION: str = "0.0.1"
    # 项目描述
    PROJECT_DESC: str = "api testing"
    # 项目作者
    PROJECT_AUTHOR: str = "Hide"

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    APP_ENV: str = "development"


settings = Settings()
