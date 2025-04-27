from fastapi import APIRouter, Depends

from app.presentation.handler.user_handler import UserHandler
from app.usecases.user.create_user_usecase import CreateUserUsecase
from app.schemas.users import UserCreateSchema


ddd_router = APIRouter()


@ddd_router.post("/ddd_user")
def create_user(
    data: UserCreateSchema,
    handler: UserHandler = Depends(UserHandler),
):
    return handler.create_user(data)
