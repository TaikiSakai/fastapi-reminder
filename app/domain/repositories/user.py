from abc import ABC, abstractmethod

from pydantic import BaseModel

from app.schemas.users import UserSchema


class CreateUserDto(BaseModel):
    user_name: str
    email: str
    role: str


class UpdateUserDto(BaseModel):
    user_name: str
    email: str
    role: str


class GetUserDto(BaseModel):
    id: int


class UserInterface(ABC):
    @abstractmethod
    def create(self, user_dto: CreateUserDto) -> UserSchema:
        pass

    @abstractmethod
    def get(self, id: int) -> UserSchema:
        pass

    @abstractmethod
    def update(self, id: int, user_dto: UpdateUserDto) -> UserSchema:
        pass

    @abstractmethod
    def delete(self, id: int) -> UserSchema:
        pass

