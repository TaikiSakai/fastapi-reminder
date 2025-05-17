from datetime import datetime

import pytest
from pytest_mock import MockFixture

from app.infrastructures.postgres.user.user_repository import UserRepository
from app.domain.user.exceptions.user import UserNotFoundError
from app.domain.user.entities.user import User
from app.domain.user.datas.user_name import UserName
from app.domain.user.datas.user_email import Email
from app.domain.user.datas.user_is_active import IsActive
from app.domain.user.datas.user_role import Role
from app.usecases.user.get_user_usecase import GetUserUsecase


class TestGetUserUsecase:
    def test_execute(self, mocker: MockFixture):
        user_repository = mocker.MagicMock(UserRepository)

        user_id = 1

        user = User(
            id=user_id,
            user_name=UserName("test_user"),
            email=Email("test_user@example.com"),
            is_active=IsActive(True),
            role=Role("admin"),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        user_repository.get_user.return_value = user

        usecase = GetUserUsecase(user_repository)
        result = usecase.execute(user_id=user_id)

        assert isinstance(result, User)

    def test_execute_user_not_found(self, mocker: MockFixture):
        user_repository = mocker.MagicMock(UserRepository)
        user_repository.get_user.return_value = None

        user_id = 1

        usecase = GetUserUsecase(user_repository)
        with pytest.raises(UserNotFoundError) as ex:
            usecase.execute(user_id=user_id)

        assert isinstance(ex.value, UserNotFoundError)
        assert str(ex.value) == f"User with ID {user_id} not found."
