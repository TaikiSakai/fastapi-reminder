from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.users import UserSchema
from app.db.database import get_db
from app.infrastructures.repositories.user_repository import UserRepository
from app.domain.repositories.user import CreateUserDto, UpdateUserDto
from user_usecase import UserUsecase


router = APIRouter()

@router.get("/user")
def get_users(id: int, db: Annotated[Session, Depends(get_db)]):
    user_repo = UserRepository(db)
    user_usecase = UserUsecase(user_repo)
    
    return user_usecase.get(id)

@router.post("/user")
def create_user(user_data: CreateUserDto, 
                db: Annotated[Session, Depends(get_db)]
) -> UserSchema:
    user_repo = UserRepository(db)
    user_usecase = UserUsecase(user_repo)

    return user_usecase.create(user_data)


@router.put("/user")
def update_user(id: int, user_data: UpdateUserDto,
                db: Annotated[Session, Depends(get_db)]
) -> UserSchema:
    user_repo = UserRepository(db)
    user_usecase = UserUsecase(user_repo)
    updated = user_usecase.update(id, user_data)
    return updated