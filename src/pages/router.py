from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.todo.router import list_todo


# показываем где находиться папка с шаблонами
templates = Jinja2Templates(directory='templates')

route = APIRouter(prefix='/todo', tags=['todo'])


@route.get('/list')
def get_todo_list(request: Request, todo: list = Depends(list_todo)):
    return templates.TemplateResponse('todo/todo.html', {'request': request, 'todo_list': todo})
