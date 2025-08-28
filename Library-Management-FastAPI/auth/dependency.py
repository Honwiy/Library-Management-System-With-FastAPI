from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, Depends, status, HTTPException
from user.models import User
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from auth.constants import SECRET_KEY, ALGORITHM
from fastapi import APIRouter, Depends, status

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)



bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/login')


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.name == username).first()
    if user and bcrypt_context.verify(password, user.password):
        return user
    return None 

def create_access_token(username: str, user_id: int, is_admin: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'is_admin': is_admin}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        is_admin: str = payload.get('is_admin')
        if username is None or user_id is None:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Couldn't validte user")
        return {"username": username, "id": user_id, "is_admin": is_admin}
    except JWTError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail='Could not validate user')

