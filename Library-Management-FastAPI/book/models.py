# Create database ORM models

from sqlalchemy import Column, Integer, Numeric, String, Date, BigInteger, SmallInteger
from database import Base


class Book(Base):
  __tablename__ = 'book'

  id = Column(Integer, primary_key=True, index=True, comment="book unique id")
  name = Column(String, nullable=False, comment="book name")
  author_id = Column(Integer, nullable=False, comment="book author id")
  category_id = Column(BigInteger, nullable=False, comment="book category id")
  sell_price = Column(Numeric(10, 2), comment="book sell price")
  stock_count = Column(Integer, comment="book stock count")
  description = Column(String, comment="book description")
  is_deleted = Column(SmallInteger, default=0)
  created_time = Column(Date)
  updated_time = Column(Date)