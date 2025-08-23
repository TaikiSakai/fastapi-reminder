import logging
from typing import Any

import boto3
from fastapi import UploadFile
from botocore.exceptions import ClientError

from app.config import settings
from app.usecases.port.aws import S3ServiceInterface


class S3Service(S3ServiceInterface):
    def __init__(self):
        self.client = boto3.client(
            's3',
            endpoint_url=settings.aws_endpoint,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
        )

    def upload_file(
        self,
        file_name: UploadFile,
        bucket: str,
        object_name: str
    ) -> bool:
        """Upload a file to an S3 bucket."""
        try:
            self.client.upload_fileobj(file_name.file, bucket, object_name)
            logging.info(f"File {file_name.filename} uploaded to {bucket}/{object_name}.")
        except ClientError as e:
            logging.error(f"Error uploading file: {e}")
            return False

        return True

    def create_presigned_url(
        self,
        bucket: str,
        object_name: str,
        expiration: int = 3600
    ) -> str | None:
        """Generate a presigned URL to share an S3 object."""
        try:
            response = self.client.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket, 'Key': object_name},
                ExpiresIn=expiration
            )
        except ClientError as e:
            logging.error(f"Error generating presigned URL: {e}")
            return None

        return response

    def create_presigned_post(
        self,
        bucket: str,
        object_name: str,
        expiration: int = 3600
    ) -> dict[str, Any] | None:
        """Generate a presigned URL for uploading an object to S3."""
        try:
            response = self.client.generate_presigned_post(
                Bucket=bucket,
                Key=object_name,
                ExpiresIn=expiration
            )
        except ClientError as e:
            logging.error(f"Error generating presigned post: {e}")
            return None

        return response


def new_s3_service() -> S3Service:
    return S3Service()
