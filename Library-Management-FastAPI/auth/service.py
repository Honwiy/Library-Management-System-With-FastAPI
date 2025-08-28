
from sqlalchemy.orm import Session
from auth.schemas import CreateUserRequest
from user.models import User
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user_service(db: Session, create_user_request: CreateUserRequest):
  user = User(
    account_number = create_user_request.account_number,
    name = create_user_request.name,
    email = create_user_request.email,
    account_balance = create_user_request.account_balance,
    password = bcrypt_context.hash(create_user_request.password),
    is_admin = create_user_request.is_admin,
    is_deleted = create_user_request.is_deleted,
    created_date = create_user_request.created_date,
    updated_date = create_user_request.updated_date,
  )
  db.add(user)
  db.commit()
  db.refresh(user)
  return user