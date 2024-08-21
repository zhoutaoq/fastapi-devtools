from fastapi import HTTPException, Header


async def verify_token(x_token: str = Header()):
    """ token验证 """
    print("x_token:", x_token)
    if x_token is None:
        raise HTTPException(status_code=401, detail="X-Token header missing")
    # 在这里进行验证 token 的逻辑，这里简单地假设 token 为 "valid_token"
    if x_token != "123456":
        raise HTTPException(status_code=403, detail="Invalid token")
    return x_token
