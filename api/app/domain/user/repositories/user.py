from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.user.entities import User
from app.domain.user.datas import IconURL


class UserRespositoryInterFace(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, id: int) -> Optional[User]:
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
