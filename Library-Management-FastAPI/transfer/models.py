# Create database ORM models

from sqlalchemy import Column, Integer, Numeric, SmallInteger, String, Date
from database import Base


class Transfer(Base):
  __tablename__ = 'transfer'

  id = Column(Integer, primary_key=True, index=True, comment="transfer unique id")
  transfer_number = Column(String, nullable=False, comment="transfer number")
  user_id = Column(Integer, nullable=False, comment="buyer user id")
  order_id = Column(Integer, nullable=False, comment="seller user id")
  amount = Column(Numeric(10, 2), comment="total price")
  type = Column(SmallInteger, default=0, comment="transfer status, 0: not paid, 1: paid, 2: cancelled, 3: completed")
  created_date = Column(Date)
  creator_id = Column(Integer, nullable=False)
  updated_date = Column(Date)
  updator_id = Column(Integer, nullable=False)

