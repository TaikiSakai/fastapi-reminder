"""Value Object for User Is Active."""

from dataclasses import dataclass


@dataclass(frozen=True)
class IsActive:
    """User Is Active Value Object."""

    value: bool

    def __post_init__(self):
        if not self.value:
            raise ValueError("User is active status cannot be empty")

    def __bool__(self) -> bool:
        return self.value
