from typing import Annotated
from sqlalchemy.orm import Session
from routers.auth import get_current_user
from starlette import status
from database import SessionLocal
from models import Users
from routers.auth import bcrypt_context
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


@router.put("/users/changepass", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(db: db_dependency, user: user_dependency, new_pass: str, retype_new_pass: str):
    if new_pass == retype_new_pass:
        user_model = get_user_info(db, user)
        if user_model is None:
            raise HTTPException(status_code=404, detail='User not found')
        user_model.hashed_password = bcrypt_context.hash(new_pass)
        db.add(user_model)
        db.commit()