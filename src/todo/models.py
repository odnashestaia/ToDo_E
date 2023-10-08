from datetime import datetime
from enum import Enum
from fastapi import Depends
from sqlalchemy import TIMESTAMP, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Session

from src.auth.models import User
from src.db import Base


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean)
    user_id = Column('user_id', ForeignKey(User.id), nullable=False)
    created_at = Column('created_at', TIMESTAMP, default=datetime.utcnow)
    # data_complete = Column(TIMESTAMP, default=datetime.utcnow)
