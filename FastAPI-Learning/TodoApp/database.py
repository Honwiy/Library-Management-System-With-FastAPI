# Connect to database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread': False})

# connect to postgresql
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/TodoApplicationDatabase' # can change to other database url

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:XUhongyu151432.@127.0.0.1:3306/TodoApplicationDatabase'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
