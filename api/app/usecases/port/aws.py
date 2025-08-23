from abc import ABC, abstractmethod
from typing import Any

from fastapi import UploadFile


class S3ServiceInterface(ABC):
    @abstractmethod
    def upload_file(
        self,
        file_name: UploadFile,
        bucket: str,
        object_name: str
    ) -> bool:
        pass

    @abstractmethod
    def create_presigned_url(
        self,
        bucket: str,
        object_name: str,
        expiration: int = 3600
    ) -> str | None:
        pass

    @abstractmethod
    def create_presigned_post(
        self,
        bucket: str,
        object_name: str,
        expiration: int = 3600
    ) -> dict[str, Any] | None:
        pass
