"""Value Object for User Name."""

from dataclasses import dataclass


@dataclass(frozen=True)
class UserName:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("User name cannot be empty")
        if len(self.value) > 100:
            raise ValueError("User name cannot exceed 100 characters")

    def __str__(self) -> str:
        return self.value
