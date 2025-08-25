from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import Annotated

router = APIRouter()

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

class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    role: str = 'user'  # default role is 'user'

@router.post("/auth", status_code=status.HTTP_201_CREATED)
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
