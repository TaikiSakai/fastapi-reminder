"""Postgres implementation of the UserRepository interface."""

from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.domain.user.repositories import UserRespositoryInterFace
from app.domain.user.entities import User
from app.infrastructures.models.users import UsersModel


class UserRepository(UserRespositoryInterFace):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: Annotated[User, User]) -> User:
        user_dto = UsersModel.from_entity(user)
        self.db.add(user_dto)
        self.db.commit()

        return user_dto.to_entity()

    def get_user(self, id: int) -> User:
        user = self.db.query(UsersModel).filter(UsersModel.id == id).first()
        if user:
            return user.to_entity()

        raise HTTPException(status_code=404, detail="User not found")

    def update_user(self, id: int, user: Annotated[User, User]) -> None:
        current_user = self.db.query(UsersModel) \
            .filter(UsersModel.id == id).first()

        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")

        user_dto = UsersModel.from_entity(user)
        current_user.email = user_dto.email
        current_user.user_name = user_dto.user_name
        current_user.role = user_dto.role
        current_user.updated_at = user_dto.updated_at

    def delete_user(self, id: int) -> bool:
        user = self.db.query(UsersModel).filter(UsersModel.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        self.db.delete(user)
        self.db.flush()

        return True

    def get_all_users(self) -> list[User]:
        users = self.db.query(UsersModel).all()
        return [user.to_entity() for user in users]


def new_user_repository(db: Session) -> UserRepository:
    """Create a new instance of UserRepository."""
    return UserRepository(db)
