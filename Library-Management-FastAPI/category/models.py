# Create database ORM models

from sqlalchemy import Column, Integer, String, Date, BigInteger
from database import Base


class Category(Base):
  __tablename__ = 'category'

  id = Column(BigInteger, primary_key=True, index=True, comment="book category unique id")
  name = Column(String, nullable=False, comment="category name")
  parent_id = Column(BigInteger, comment="parent category id")
  remark = Column(String) 
  created_time = Column(Date)
  created_by = Column(String, default=1)
  updated_time = Column(Date)
  updated_by = Column(String)