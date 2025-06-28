from abc import abstractmethod

from app.domain.user.datas import (
    UserName,
    Email,
    Role,
)
from app.domain.user.entities.user import User
from app.domain.user.repositories.user import UserRespositoryInterFace
from app.domain.user.exceptions.user import UserNotFoundError


class UpdateUserUseCaseInterFace:
    @abstractmethod
    def execute(
            self,
            id: int,
            user_name: UserName,
            email: Email,
            role: Role,
    ) -> User:
        pass


class UpdateUserUsecase(UpdateUserUseCaseInterFace):
    def __init__(self, user_repository: UserRespositoryInterFace) -> None:
        self.user_repository = user_repository

    def execute(
            self,
            id: int,
            user_name: UserName | None,
            email: Email | None,
            role: Role | None,
    ) -> User:
        # Check if the user exists
        user = self.user_repository.get_user(id)
        if not user:
            raise UserNotFoundError(id)

        # Update the user
        if user_name is not None:
            user.update_user_name(user_name)
        if email is not None:
            user.update_email(email)
        if role is not None:
            user.update_role(role)

        self.user_repository.update_user(id, user)

        return user


def new_update_user_usecase(
        user_repository: UserRespositoryInterFace
) -> UpdateUserUsecase:
    return UpdateUserUsecase(user_repository)
