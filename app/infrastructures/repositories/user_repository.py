from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

from app.domain.repositories.user import GetUserDto, CreateUserDto, UpdateUserDto, UserInterface
from app.schemas.users import UserSchema
from app.infrastructures.models.users import UsersModel


class UserRepository(UserInterface):
    def __init__(self, db: Session):
        self.db = db

    def create(
            self,
            user_dto: Annotated[CreateUserDto, Depends(CreateUserDto)]
    ) -> UserSchema:
        user = UsersModel(**user_dto.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get(self, id: int) -> UserSchema:
        user = self.db.query(UsersModel).filter(UsersModel.id == id).first()
        return user

    def update(
            self,
            id: int,
            user_dto: Annotated[UpdateUserDto, Depends(UpdateUserDto)]
    ) -> UserSchema:
        user: UsersModel = self.db.query(UsersModel).filter(UsersModel.id == id).first()

        if user:
            user.user_name = user_dto.user_name
            user.email = user_dto.email
            user.role = user_dto.role
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            return user

        raise HTTPException(status_code=404, detail="User not found")

    def delete(self, id: int) -> UserSchema:
        user = self.db.query(UsersModel).filter(UsersModel.id == id).first()

        if user:
            self.db.delete(user)
            self.db.commit()

            return user

        return HTTPException(status_code=404, detail="User not found")
