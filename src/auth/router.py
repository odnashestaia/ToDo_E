from fastapi import APIRouter, Depends

from fastapi_users import FastAPIUsers
from sqlalchemy import Integer
from src.auth.schemas import UserCreate, UserRead, UserUpdate

from src.db import get_async_session
from .models import User

from .service import get_user_manager, auth_backend


fastapi_users = FastAPIUsers[User, Integer](
    get_user_manager,
    [auth_backend],
)


route = APIRouter()

route.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"]
)

route.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

route.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
