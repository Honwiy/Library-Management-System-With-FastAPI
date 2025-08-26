from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = '31e54359a62ee1298f1e72aaa3b3af6da3e74d38d376dff7be6554e60865089f'
ALGORITHM = 'HS256'

class Token(BaseModel):
  access_token: str
  token_type: str

  
class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    role: str = 'user'  # default role is 'user'


# Create the database tables

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Database dependency
db_dependency = Annotated[Session, Depends(get_db)]



bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/login')


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(Users).filter(Users.username == username).first()
    if user and bcrypt_context.verify(password, user.hashed_password):
        return user
    return None 

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Couldn't validte user")
        return {"username": username, "id": user_id, "user_role": user_role}
    except JWTError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail='Could not validate user')



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):

  create_user_request = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    role=create_user_request.role,
    hashed_password=bcrypt_context.hash(create_user_request.password),
    is_active=True
  )

  db.add(create_user_request)
  db.commit()
  db.refresh(create_user_request)
  return create_user_request


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}
