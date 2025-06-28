from abc import abstractmethod

from app.domain.user.exceptions.user import UserNotFoundError
from app.domain.user.repositories.user import UserRespositoryInterFace


class DeleteUserUseCaseInterFace:
    @abstractmethod
    def execute(self, user_id: int) -> bool:
        pass


class DeleteUserUsecase(DeleteUserUseCaseInterFace):
    def __init__(self, user_repository: UserRespositoryInterFace) -> None:
        self.user_repository = user_repository

    def execute(self, user_id: int) -> bool:
        user = self.user_repository.get_user(user_id)

        if user is None:
            raise UserNotFoundError(user_id)

        return self.user_repository.delete_user(user_id)


def new_delete_user_usecase(
        user_repository: UserRespositoryInterFace
) -> DeleteUserUsecase:
    return DeleteUserUsecase(user_repository)
