from datetime import timedelta
from fastapi import Depends, status, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from auth.dependency import authenticate_user, create_access_token


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

async def user_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = create_access_token(user.name, user.id, user.is_admin, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}