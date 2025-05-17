from datetime import datetime

import pytest
from pytest_mock import MockFixture

from app.infrastructures.postgres.user.user_repository import UserRepository
from app.domain.user.exceptions.user import NoUsersRegisteredError
from app.domain.user.entities.user import User
from app.domain.user.datas.user_name import UserName
from app.domain.user.datas.user_email import Email
from app.domain.user.datas.user_is_active import IsActive
from app.domain.user.datas.user_role import Role
from app.usecases.user.get_all_users_usecase import GetAllUsersUsecase


class TestGetAllUserUsecase:
    def test_execute(self, mocker: MockFixture):
        user_repository = mocker.MagicMock(UserRepository)

        user_id = 1
        user_id_2 = 2

        user = User(
            id=user_id,
            user_name=UserName("test_user"),
            email=Email("test_user@example.com"),
            is_active=IsActive(True),
            role=Role("admin"),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        user_2 = User(
            id=user_id_2,
            user_name=UserName("test_user_2"),
            email=Email("test_user_2@example.com"),
            is_active=IsActive(True),
            role=Role("user"),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        user_repository.get_all_users.return_value = [user, user_2]

        usecase = GetAllUsersUsecase(user_repository)
        result = usecase.execute()

        assert isinstance(result, list)
        assert result[0] == user
        assert result[1] == user_2

    def test_execute_no_users_registered(self, mocker: MockFixture):
        user_repository = mocker.MagicMock(UserRepository)
        user_repository.get_all_users.return_value = None

        usecase = GetAllUsersUsecase(user_repository)
        with pytest.raises(NoUsersRegisteredError) as ex:
            usecase.execute()

        assert isinstance(ex.value, NoUsersRegisteredError)
        assert str(ex.value) == "No users registered"
