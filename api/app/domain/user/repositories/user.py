from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from fastapi_pagination import Page

from app.domain.user.entities import User
from app.domain.user.datas import (
    UserName,
    Role,
    IconURL
)


class UserRespositoryInterFace(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_user(
        self,
        user_name: UserName | None,
        role: Role | None,
        created_at_from: datetime | None,
        created_at_to: datetime | None,
    ) -> Page[User]:
        pass

    @abstractmethod
    def update_user(self, id: int, user: User) -> None:
        pass

    @abstractmethod
    def update_user_icon_url(self, id: int, icon_url: IconURL) -> IconURL | None:
        pass

    @abstractmethod
    def delete_user(self, id: int) -> bool:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass
