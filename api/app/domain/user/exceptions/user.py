class UserNotFoundError(Exception):
    """Exception raised when a user is not found."""

    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} not found.")


class NoUsersRegisteredError(Exception):
    """Exception raised when no users are registered."""

    def __init__(self, message: str):
        super().__init__(message)
