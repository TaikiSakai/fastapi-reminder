from abc import abstractmethod

from app.domain.user.exceptions.user import UserNotFoundError
from app.domain.user.entities.user import User
from app.domain.user.repositories.user import UserRespositoryInterFace


class GetUserUseCaseInterFace:
    @abstractmethod
    def execute(self, user_id: int) -> User:
        pass


class GetUserUsecase(GetUserUseCaseInterFace):
    def __init__(self, user_repository: UserRespositoryInterFace) -> None:
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        user = self.user_repository.get_user(user_id)

        if user is None:
            raise UserNotFoundError(user_id)

        return user


def new_get_user_usecase(
        user_repository: UserRespositoryInterFace
) -> GetUserUsecase:
    return GetUserUsecase(user_repository)
