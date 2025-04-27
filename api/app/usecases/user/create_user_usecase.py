
from abc import abstractmethod

from app.domain.user.entities.user import User
from app.domain.user.repositories.user import UserRespositoryInterFace
from app.domain.user.datas import (
    Email,
    UserName,
    IsActive,
    Role,
)


class CreateUserUseCaseInterFace:
    @abstractmethod
    def execute(
            self,
            email: Email,
            user_name: UserName,
            is_active: IsActive,
            role: Role
    ) -> User:
        pass


class CreateUserUsecase(CreateUserUseCaseInterFace):
    def __init__(self, user_repository: UserRespositoryInterFace) -> None:
        self.user_repository = user_repository

    def execute(
            self,
            email: Email,
            user_name: UserName,
            is_active: IsActive,
            role: Role
    ) -> User:
        user = User(
            id=None,  # ID will be assigned by the database
            email=email,
            user_name=user_name,
            is_active=is_active,
            role=role
        )
        user = self.user_repository.create_user(user)

        return user


def new_create_user_usecase(
        user_repository: UserRespositoryInterFace
) -> CreateUserUsecase:
    return CreateUserUsecase(user_repository)
