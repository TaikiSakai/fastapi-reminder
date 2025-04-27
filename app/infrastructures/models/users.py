from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base
from app.domain.user.entities.user import User
from app.domain.user.datas import (
    Email,
    UserName,
    IsActive,
    Role
)


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime, nullable=False)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            email=Email(self.email),
            user_name=UserName(self.user_name),
            is_active=IsActive(self.is_active),
            role=Role(self.role),
        )

    @staticmethod
    def from_entity(user: User) -> 'UsersModel':
        return UsersModel(
            id=user.id,
            email=user.email.value,
            user_name=user.user_name.value,
            is_active=user.is_active.value,
            role=user.role.value,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
