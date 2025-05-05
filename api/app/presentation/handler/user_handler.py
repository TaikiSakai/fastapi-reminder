from typing import List

from fastapi import Depends, APIRouter

from app.domain.user.datas import (
    UserName,
    Email,
    IsActive,
    Role,
)
from app.infrastructures.di.injection import (
    get_create_user_usecase,
    get_user_usecase,
    get_all_users_usecase,
)
from app.usecases.user.create_user_usecase import CreateUserUsecase
from app.usecases.user.get_user_usecase import GetUserUsecase
from app.usecases.user.get_all_users_usecase import GetAllUsersUsecase
from app.schemas.users import UserCreateSchema, UserSchema


router = APIRouter()

@router.get("/user/{user_id}")
def get_user(
    user_id: int,
    usecase: GetUserUsecase = Depends(get_user_usecase)
) -> UserSchema:
    user = usecase.execute(user_id=int(user_id))

    return UserSchema.from_entity(user)


@router.get("/users")
def get_users(
    usecase: GetAllUsersUsecase = Depends(get_all_users_usecase)
) -> List[UserSchema]:
    users = usecase.execute()

    return [UserSchema.from_entity(user) for user in users]


@router.post("/user")
def create_user(
    data: UserCreateSchema,
    usecase: CreateUserUsecase = Depends(get_create_user_usecase)
) -> UserSchema:
    user_name = UserName(data.user_name)
    email = Email(data.email)
    is_active = IsActive(True)
    role = Role(data.role)

    user = usecase.execute(
        email=email,
        user_name=user_name,
        is_active=is_active,
        role=role
    )

    return UserSchema.from_entity(user)
