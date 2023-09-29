import uuid
from fastapi import APIRouter

from fastapi_users import FastAPIUsers

from src.db import User

from .service import get_user_manager, auth_backend


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


route = APIRouter(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth',
)
