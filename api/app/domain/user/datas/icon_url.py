"""Value Object for User Icon URL."""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class IconURL:
    """User Icon URL Value Object."""

    value: UUID

    @staticmethod
    def generate() -> 'IconURL':
        """Generate a new IconURL with a unique UUID."""
        return IconURL(value=uuid4())

    def __str__(self) -> str:
        return str(self.value)
