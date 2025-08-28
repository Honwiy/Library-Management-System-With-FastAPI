from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from user.schemas import Token
from fastapi import APIRouter, Depends
from dependency import db_dependency
from user.service import user_login


router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
  return await user_login(form_data, db)
