from typing import Any

from pydantic import BaseModel, Field


from app.domain.user.entities import User


class UserSchema(BaseModel):
    id: int | None
    user_name: str
    email: str
    role: str

    @staticmethod
    def from_entity(user: User) -> 'UserSchema':
        return UserSchema(
            id=user.id,
            user_name=str(user.user_name),
            email=str(user.email),
            role=user.role
        )


class UserCreateSchema(BaseModel):
    user_name: str = Field(min_length=1, max_length=100)
    email: str
    role: str


class UserUpdateSchema(BaseModel):
    user_name: str | None = Field(min_length=1, max_length=100)
    email: str | None
    role: str | None


class SearchUserSchema(BaseModel):
    user_name: str | None = Field(default=None, min_length=1, max_length=100)
    role: str | None = Field(default=None)
    created_at_from: str | None = Field(default=None)
    created_at_to: str | None = Field(default=None)


class UserResponeSchema(BaseModel):
    id: int
    user_name: str
    email: str

    class Config:
        orm_mode = True


class SearchUserResponseSchema(BaseModel):
    users: list[UserResponeSchema]
    total: int
    page: int
    size: int


class S3PresignedPostResponseField(BaseModel):
    key: str
    AwsAccessKeyId: str
    policy: str
    signature: str


class S3PresignedPostResponseMessage(BaseModel):
    url: str
    fields: S3PresignedPostResponseField


class UserIconResponseSchema(BaseModel):
    message: S3PresignedPostResponseMessage

    @staticmethod
    def from_presigned_post_response(response: dict[str, Any]) -> 'UserIconResponseSchema':
        return UserIconResponseSchema(
            message=S3PresignedPostResponseMessage(
                url=response['url'],
                fields=S3PresignedPostResponseField(
                    key=response['fields']['key'],
                    AwsAccessKeyId=response['fields']['AWSAccessKeyId'],
                    policy=response['fields']['policy'],
                    signature=response['fields']['signature']
                )
            )
        )
