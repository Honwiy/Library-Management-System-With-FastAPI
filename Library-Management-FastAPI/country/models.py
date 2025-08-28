# Create database ORM models

from sqlalchemy import Column, Integer, String, Date
from database import Base


class Country(Base):
  __tablename__ = 'country'

  id = Column(Integer, primary_key=True, index=True, comment="country unique id")
  name = Column(String, nullable=False, comment="country name")
  code = Column(String, unique=True, nullable=False, comment="country code, eg CN, US")
  description = Column(String) 
  created_date = Column(Date)
  updated_date = Column(Date)