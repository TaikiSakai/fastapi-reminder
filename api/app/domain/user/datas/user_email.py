"""Value Object for User Email."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    """User Email Value Object."""

    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("User email cannot be empty")
        if len(self.value) > 255:
            raise ValueError("User email cannot exceed 255 characters")

    def __str__(self) -> str:
        return self.value
