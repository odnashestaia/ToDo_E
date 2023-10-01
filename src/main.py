from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi_redis_cache import FastApiRedisCache, cache

from redis import asyncio as aioredis

from src.config import REDIS_HOST

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


@app.on_event("startup")
async def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=REDIS_HOST,
        prefix="fastapi_cache"
        # response_header="X-MyAPI-Cache",
        # ignore_arg_types=[Request, Response, Session]
    )

    # почему-то не рабоате
    # redis = aioredis.from_url('redis://localhost')  # подключение к редису

    # # инициализация редиса
    # # prefix с каким названием будет храниться кеш
    # FastAPICache.init(RedisBackend(redis), prefix='fastapi_cache')
