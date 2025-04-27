from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.infrastructures.postgres.user.user_repository import (
    UserRepository,
    new_user_repository,
)
from app.usecases.user.create_user_usecase import (
    CreateUserUsecase,
    new_create_user_usecase,
)
from app.usecases.user.get_user_usecase import (
    GetUserUsecase,
    new_get_user_usecase,
)


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    """Get a new instance of UserRepository."""
    return new_user_repository(db)


def get_create_user_usecase(
    user_repository: UserRepository = Depends(get_user_repository)
) -> CreateUserUsecase:
    """Get a new instance of CreateUserUsecase."""
    return new_create_user_usecase(user_repository)


def get_user_usecase(
    user_repository: UserRepository = Depends(get_user_repository)
) -> GetUserUsecase:
    """Get a new instance of UserUsecase."""
    return new_get_user_usecase(user_repository)
