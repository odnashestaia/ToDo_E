from fastapi import Depends, Form, Request, APIRouter
from fastapi.encoders import jsonable_encoder

from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from src.auth.router import fastapi_users
from src.auth.models import User
from src.db import get_async_session

from .models import Todo

router_todo = APIRouter(prefix='/todo_docs', tags=['todo'])


current_user = fastapi_users.current_user()


@router_todo.get("/list")
async def list_todo(user: User = Depends(current_user), session: Session = Depends(get_async_session)):
    stmt = select(Todo).order_by(Todo.user_id == user.id)
    result = await session.execute(stmt)
    return result.scalars().all()


@router_todo.post('/add')
async def add_todo(title: str = Form(...), is_complete: bool = Form(...), session: Session = Depends(get_async_session), user: User = Depends(current_user)):
    new_todo = Todo(title=title,
                    is_complete=is_complete, user_id=user.id)
    session.add(new_todo)
    await session.commit()

    return {'result': 'todo was add'}


@router_todo.put("/change/{id_todo}")
async def update_todo(id_todo: int, title: str = Form(...), is_complete: bool = Form(...), session: Session = Depends(get_async_session),  user: User = Depends(current_user)):
    stmt = update(Todo).where(Todo.id == id_todo)\
        .values({"title": title, 'is_complete': is_complete})

    await session.execute(stmt)
    await session.commit()

    return {'result': "task was change"}


@router_todo.delete("/delete/{id_todo}")
async def delete_todo(id_todo: int, session: Session = Depends(get_async_session), user: User = Depends(current_user)):
    stmt = delete(Todo).where(Todo.id == id_todo)
    await session.execute(stmt)
    await session.commit()
    return {'result':
            {'text': "task was deleted",
             'id': {id_todo}}}
