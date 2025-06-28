from datetime import datetime
from typing import Optional

from app.domain.user.datas import (
    Email,
    Role,
    UserName,
    IsActive,
)


class User:
    def __init__(
            self,
            email: Email,
            user_name: UserName,
            is_active: IsActive,
            role: Role,
            id: Optional[int] = None,
            created_at: datetime = datetime.now(),
            updated_at: datetime = datetime.now()
    ) -> None:
        self._id: int | None = id
        self._email: Email = email
        self._user_name: UserName = user_name
        self._is_active: IsActive = is_active
        self._role: Role = role
        self._created_at: datetime = created_at
        self._updated_at: datetime = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, User):
            return self._id == obj._id

        return False

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def email(self) -> Email:
        return self._email

    @property
    def user_name(self) -> UserName:
        return self._user_name

    @property
    def is_active(self) -> IsActive:
        return self._is_active

    @property
    def role(self) -> Role:
        return self._role

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at
    
    def update_user_name(self, new_user_name: UserName) -> None:
        self._user_name = new_user_name
        self._updated_at = datetime.now()

    def update_email(self, new_email: Email) -> None:
        self._email = new_email
        self._updated_at = datetime.now()

    def update_role(self, new_role: Role) -> None:
        self._role = new_role
        self._updated_at = datetime.now()

    @staticmethod
    def create(
            id: int | None,
            email: Email,
            user_name: UserName,
            is_active: IsActive,
            role: Role,
            created_at: datetime | None,
            updated_at: datetime | None
    ) -> "User":
        return User(
            id=id,
            email=email,
            user_name=user_name,
            is_active=is_active,
            role=role,
            created_at=created_at or datetime.now(),
            updated_at=updated_at or datetime.now()
        )
