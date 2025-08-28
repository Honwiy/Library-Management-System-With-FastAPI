from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends

# Create the database tables

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Database dependency
db_dependency = Annotated[Session, Depends(get_db)]