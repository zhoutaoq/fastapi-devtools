#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import bcrypt


def get_password_hash(password: str):
    if not password:  # 检查密码是否为None或空字符串
        return None
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码与哈希密码是否匹配。

    :param plain_password: 用户输入的明文密码。
    :param hashed_password: 数据库中存储的哈希密码。
    :return: 布尔值，如果密码匹配返回True，否则返回False。
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
