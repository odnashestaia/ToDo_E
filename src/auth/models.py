from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String

from src.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column('id', Integer,  primary_key=True)
    username = Column('username', String, nullable=False)
