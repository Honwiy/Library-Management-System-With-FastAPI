# Create database ORM models

from sqlalchemy import Column, Integer, Numeric, String, SmallInteger, Date
from database import Base


class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, index=True)
  account_number = Column(String(45), nullable=False)
  name = Column(String(100), nullable=False)
  password = Column(String(100), nullable=False) 
  email = Column(String(45), nullable=False, unique=True)
  account_balance = Column(Numeric(10, 2), default=0.00)
  is_admin = Column(SmallInteger, default=0)
  is_deleted = Column(SmallInteger, default=0)
  created_date = Column(Date)
  updated_date = Column(Date)

