# 定义秘钥和算法
from datetime import datetime, timedelta

import jwt

secret_key = "abcd12345@abcdef"
algorithm = "HS256"


def jwtGenerator(secret: str = secret_key) -> str:
    # 构造 payload
    payload = {
        "uid": 1234567,  # 主题，通常是用户的唯一标识
        "iat": datetime.utcnow(),  # 签发时间
        "exp": datetime.utcnow() + timedelta(minutes=30),  # 过期时间
        "data": {"user_name": "张三", "uid": 1234567, "phone": "17600000000"}  # 自定义的数据
    }
    # 生成 JWT
    return jwt.encode(payload, secret, algorithm=algorithm)


def parseToken(jwtToken: str, secret: str = secret_key) -> str:
    """ 解析token """
    try:
        return jwt.decode(jwtToken, secret, algorithms=[algorithm])
    except jwt.ExpiredSignatureError:
        print("JWT has expired.")
        return ""
    except jwt.InvalidTokenError:
        print("Invalid JWT.")
        return ""


class JwtManageUtil():
    def __init__(self, secret):
        self.secret_key = secret

    def decode(self, token: str):
        return parseToken(token, self.secret_key)


if __name__ == '__main__':
    token = jwtGenerator()
    # 验证token
    parseToken = parseToken(token)
    print("parseToken:", token)
    print("parseToken:", parseToken)
