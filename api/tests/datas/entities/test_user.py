from datetime import datetime

from app.domain.user.entities.user import User
from app.domain.user.datas.user_name import UserName
from app.domain.user.datas.user_email import Email
from app.domain.user.datas.user_is_active import IsActive
from app.domain.user.datas.user_role import Role


class TestUser:
    def test_user_init(self):
        user = User(
            id=1,
            user_name=UserName("test_user"),
            email=Email("test_user@example.com"),
            is_active=IsActive(True),
            role=Role("admin"),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        user_without_id = User.create(
            id=None,
            user_name=UserName("test_user_2"),
            email=Email("test_user_2@example.com"),
            is_active=IsActive(True),
            role=Role("admin"),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        assert isinstance(user, User)
        assert isinstance(user_without_id, User)
