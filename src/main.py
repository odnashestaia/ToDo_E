from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.todo.router import router_todo
from src.auth.router import route as router_auth

app = FastAPI()

# передаем путь к файлам статики
app.mount("/static", StaticFiles(directory="static"), name="static")

# передаем к файлам шаблона
templates = Jinja2Templates(directory='templates')


""" импорт модулей """

app.include_router(router_todo)
app.include_router(router_auth)
