
from abc import abstractmethod

from app.domain.user.exceptions.user import NoUsersRegisteredError
from app.domain.user.entities.user import User
from app.domain.user.repositories.user import UserRespositoryInterFace


class GetAllUsersUseCaseInterFace:
    @abstractmethod
    def execute(self) -> list[User]:
        pass


class GetAllUsersUsecase(GetAllUsersUseCaseInterFace):
    def __init__(self, user_repository: UserRespositoryInterFace) -> None:
        self.user_repository = user_repository

    def execute(self) -> list[User]:
        users = self.user_repository.get_all_users()

        if not users:
            raise NoUsersRegisteredError("No users registered")

        return users


def new_get_all_users_usecase(
        user_repository: UserRespositoryInterFace
) -> GetAllUsersUsecase:
    return GetAllUsersUsecase(user_repository)
