from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.user.entities import User


class UserRespositoryInterFace(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, id: int) -> bool:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass
