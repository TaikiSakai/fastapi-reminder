"""Value Object for User Role."""

from enum import Enum


class Role(str, Enum):

    USER = "user"
    ADMIN = "admin"

    def __str__(self) -> str:
        return self.value
