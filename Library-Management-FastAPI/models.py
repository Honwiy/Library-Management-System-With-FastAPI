# Create database ORM models

from sqlalchemy import Numeric, Column, Integer, String, ForeignKey, SmallInteger, Date
from database import Base


class BookNfc(Base):
  __tablename__ = 'book_nfc'

  id = Column(Integer, primary_key=True, nullable=False, index=True)
  book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
  nfc_number = Column(String, nullable=False)
  status = Column(SmallInteger, default=1, comment='0: stored, 1: sold, 2: Broken')
  is_deleted = Column(SmallInteger, default=0)
  created_date = Column(Date)
  updated_date = Column(Date)


class OrderBook(Base):
  __tablename__ = 'order_book'

  id = Column(Integer, primary_key=True, nullable=False, index=True)
  order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
  book_nfc_id = Column(Integer, ForeignKey('book_nfc.id'), nullable=False)
  unit_price = Column(Numeric(10, 2), nullable=False)
  book_name = Column(String, nullable=False)
  book_category_id = Column(Integer, nullable=False)
  status = Column(SmallInteger, default=0, comment='0: normal, 1: refunding, 2: refunded')
  created_date = Column(Date)
  updated_date = Column(Date)


class UserBook(Base):
  __tablename__ = 'user_book'

  id = Column(Integer, primary_key=True, nullable=False, index=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
  book_nfc_id = Column(Integer, ForeignKey('book_nfc.id'), nullable=True)
  status = Column(SmallInteger, default=0, comment='0: favorited, 1: bought, 2: borrowed')
  created_date = Column(Date)