from typing import Annotated
from sqlalchemy.orm import Session
from routers.auth import get_current_user
from starlette import status
from database import SessionLocal
from models import Users
from pydantic import BaseModel, Field
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix='/user',
    tags=['user']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


def get_user_info(db, user):
    user_model = db.query(Users).\
        filter(Users.username == user.get('username')).first()

    return user_model

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed.')
    user_model = get_user_info(db, user)
    if user_model is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user_model


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(db: db_dependency, user: user_dependency, user_verification: UserVerification):
    
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    
    user_model = db.query(Users).\
        filter(Users.id == user.get('id')).first()
    
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()


@router.put("/phone_number", status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(db: db_dependency, user: user_dependency, phone_number):

    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    user_model.phone_number = phone_number

    db.add(user_model)
    db.commit()


