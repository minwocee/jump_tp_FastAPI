# DB 연결 파일

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

DB_URL = f'mysql://root:{os.environ["PASSWORD"]}@{os.environ["HOST"]}:{os.environ["PORT"]}/{os.environ["DATABASE"]}'
print(DB_URL)
# DB_URL = "sqlite:///./myapi.db"
# engine = create_engine(
#     DB_URL, connect_args={'check_same_thread': False}
# )
# print(DB_URL)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()


'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import pymysql  # Add this line

import dotenv
import os

# This line should be added right after importing pymysql.
pymysql.install_as_MySQLdb()

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

DB_URL = f'mysql://{os.environ["USERNAME"]}:{os.environ["PASSWORD"]}@{os.environ["HOST"]}:{os.environ["PORT"]}/{os.environ["DATABASE"]}'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    print(DB_URL)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
'''