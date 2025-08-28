# Create database ORM models

from sqlalchemy import Column, Integer, Numeric, SmallInteger, String, Date
from database import Base


class Order(Base):
  __tablename__ = 'order'

  id = Column(Integer, primary_key=True, index=True, comment="order unique id")
  order_number = Column(String, nullable=False, comment="order number")
  buyer_id = Column(Integer, nullable=False, comment="buyer user id")
  seller_id = Column(Integer, nullable=False, comment="seller user id")
  total_price = Column(Numeric(10, 2), comment="total price")
  status = Column(SmallInteger, default=0, comment="order status, 0: not paid, 1: paid, 2: cancelled, 3: completed")
  created_date = Column(Date)
  creator_id = Column(Integer, nullable=False)
  updated_date = Column(Date)
  updator_id = Column(Integer, nullable=False)

