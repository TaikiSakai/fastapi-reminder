"""Postgres implementation of the UserRepository interface."""

from typing import Annotated, Optional

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

    def get_user(self, id: int) -> Optional[User]:
        user = self.db.query(UsersModel).filter(UsersModel.id == id).first()
        if user:
            return user.to_entity()

        raise HTTPException(status_code=404, detail="User not found")

    def update_user(self, user: Annotated[User, User]) -> User:
        pass

    def delete_user(self, id: int) -> bool:
        pass

    def get_all_users(self) -> list[User]:
        users = self.db.query(UsersModel).all()
        return [user.to_entity() for user in users]


def new_user_repository(db: Session) -> UserRepository:
    """Create a new instance of UserRepository."""
    return UserRepository(db)
