from enum import Enum
from fastapi import Depends
from sqlalchemy import Column, Integer, String


from src.auth.models import User
from src.db import Base


class IsComplete(str, Enum):
    complete = 'Complete'
    in_progress = 'In progress'
    not_complete = 'Not complete'


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Depends(IsComplete)
    user_id = Depends(User)
