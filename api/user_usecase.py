from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.database import get_db
from app.schemas.users import UserSchema, UserCreateSchema, UserUpdateSchema
from app.infrastructures.repositories.user_repository import UserRepository

db_dependency = Annotated[Session, Depends(get_db)]


class UserUsecase:
    def __init__(self, user_repo: Annotated[UserRepository, Depends(UserRepository)]):
        self.user_repo = user_repo

    def create(self, user_data: UserCreateSchema) -> UserSchema:
        return self.user_repo.create(user_data)

    def get(self, id: int) -> UserSchema:
        return self.user_repo.get(id)

    def update(self, id: int, user_data: UserUpdateSchema) -> UserSchema:
        return self.user_repo.update(id, user_data)

    def delete(self, id: int) -> UserSchema:
        return self.user_repo.delete(id)
