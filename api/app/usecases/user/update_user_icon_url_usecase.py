from typing import Any
from abc import abstractmethod

from fastapi import UploadFile

from app.domain.user.repositories.user import UserRespositoryInterFace
from app.domain.user.exceptions.user import UserNotFoundError
from app.usecases.port.aws import S3ServiceInterface


class UpdateUserIconURLUsecaseInterface:
    @abstractmethod
    def execute(self, id: int, icon_image: UploadFile) -> dict[str, Any] | None:
        pass


class UpdateUserIconURLUsecase(UpdateUserIconURLUsecaseInterface):
    def __init__(
        self,
        user_repository: UserRespositoryInterFace,
        s3_service: S3ServiceInterface
    ) -> None:
        self.user_repository = user_repository
        self.s3_service = s3_service

    def execute(self, id: int, icon_image: UploadFile) -> dict[str, Any] | None:
        user = self.user_repository.get_user(id)
        if not user:
            raise UserNotFoundError(id)

        icon_url = user.add_icon_url()

        url = self.s3_service.create_presigned_post(
            bucket="test",
            object_name=f'{icon_url}{icon_image.filename}'
        )

        # Update the user's icon URL
        user.update_icon_url(icon_url)
        self.user_repository.update_user_icon_url(id, icon_url)

        return url


def new_update_user_icon_url_usecase(
    user_repository: UserRespositoryInterFace,
    aws_service: S3ServiceInterface,
) -> UpdateUserIconURLUsecase:
    return UpdateUserIconURLUsecase(user_repository, aws_service)
