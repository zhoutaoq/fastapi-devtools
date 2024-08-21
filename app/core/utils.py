#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
import secrets

def generate_secret_key(prefix: str, nbytes: int = 32) -> str:
    # 生成 nbytes 随机字节
    random_bytes = secrets.token_bytes(nbytes)

    # 将随机字节转换为 base64 编码的字符串
    encoded_bytes = base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')

    # 添加前缀并返回
    return f"{prefix}{encoded_bytes}"


def hide_secret_key(secret_key: str) -> str:
    # 保留前6个字符，隐藏中间的字符，保留最后4个字符
    if len(secret_key) > 10:  # 确保密钥长度足够
        return f"{secret_key[:3]}****{secret_key[-4:]}"
    return secret_key  # 如果密钥过短，不进行修改
