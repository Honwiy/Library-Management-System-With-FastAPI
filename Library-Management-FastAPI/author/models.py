# Create database ORM models

from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from database import Base



class Author(Base):
  __tablename__ = 'author'

  id = Column(Integer, primary_key=True, index=True, comment="author unique id")
  name = Column(String, nullable=False)
  country_id = Column(String, ForeignKey('country.id'), nullable=False)
  description = Column(String)
  created_date = Column(DateTime)
  updated_date = Column(DateTime)
