from datetime import datetime
from abc import abstractmethod
from fastapi_pagination import Page

from app.domain.user.datas import UserName, Role
from app.domain.user.exceptions.user import NoUsersRegisteredError
from app.domain.user.entities.user import User
from app.domain.user.repositories.user import UserRespositoryInterFace


class FindUserUseCaseInterFace:
    @abstractmethod
    def execute(
        self,
        user_name: UserName | None,
        role: Role | None,
        created_at_from: datetime | None,
        created_at_to: datetime | None,
    ) -> Page[User]:
        pass


class FindUserUsecase(FindUserUseCaseInterFace):
    def __init__(self, user_repository: UserRespositoryInterFace) -> None:
        self.user_repository = user_repository

    def execute(
        self,
        user_name: UserName | None,
        role: Role | None,
        created_at_from: datetime | None,
        created_at_to: datetime | None,
    ) -> Page[User]:
        users = self.user_repository.find_user(
            user_name,
            role,
            created_at_from,
            created_at_to
        )

        if not users:
            raise NoUsersRegisteredError("No users registered")

        return users


def new_get_find_user_usecase(
        user_repository: UserRespositoryInterFace
) -> FindUserUsecase:
    return FindUserUsecase(user_repository)
