from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import RegisterRequest


# 创建用户
def create_user(db: Session, user_in: RegisterRequest):
    hashed_password = get_password_hash(user_in.password)

    user = User(
        id=str(uuid4()),
        username=user_in.username,
        email=user_in.email,
        phone_number=user_in.phone_number,
        hashed_password=hashed_password,
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise ValueError("The username or email is already registered.")


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def update_user(db: Session, user_id: str, user_update: dict):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db_session: Session, email: str):
    return db_session.query(User).filter(User.email == email).first()


def get_user_by_phone(db_session: Session, country_code: str, phone_number: str):
    return db_session.query(User).filter(User.country_code == country_code, User.phone_number == phone_number).first()
