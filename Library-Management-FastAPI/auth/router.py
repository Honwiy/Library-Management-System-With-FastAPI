
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import SessionLocal
from auth.schemas import CreateUserRequest
from auth.service import create_user_service


router = APIRouter(
  prefix='/auth',
  tags=['auth']
)


# Create the database tables

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Database dependency
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
  return create_user_service(db, create_user_request)