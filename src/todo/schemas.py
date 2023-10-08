from datetime import datetime
from pydantic import BaseModel

from src.auth.models import User


class TodoSchema(BaseModel):
    title: str
    is_complete: bool = False
