from fastapi import Depends, Request, APIRouter

from sqlalchemy.orm import Session

from src.db import get_async_session
# from src.main import templates

router_todo = APIRouter(prefix='/todo', tags=['todo'])


@router_todo.get('/')
def home(request: Request, session: Session = Depends(get_async_session)):
    pass
