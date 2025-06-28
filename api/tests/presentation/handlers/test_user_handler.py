import pytest
from pytest_mock import MockFixture
from unittest.mock import MagicMock
from app.presentation.handler import user_handler
from app.schemas.users import UserCreateSchema, UserUpdateSchema

class TestUserHandler:
    class TestGetUser:
        def test_get_user(self, mocker: MockFixture):
            mock_user = MagicMock(id=1, user_name="test_user", email="test_user@example.com", role="admin")
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_user_usecase")
            mock_usecase.return_value.execute.return_value = mock_user
            result = user_handler.get_user(1, mock_usecase.return_value)
            assert result.id == 1
            assert result.user_name == "test_user"
            assert result.email == "test_user@example.com"
            assert result.role == "admin"

    class TestGetUsers:
        def test_get_users(self, mocker: MockFixture):
            mock_users = [
                MagicMock(id=1, user_name="test_user", email="test_user@example.com", role="admin"),
                MagicMock(id=2, user_name="test_user2", email="test2@example.com", role="user")
            ]
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_all_users_usecase")
            mock_usecase.return_value.execute.return_value = mock_users
            result = user_handler.get_users(mock_usecase.return_value)
            assert len(result) == 2
            assert result[0].id == 1
            assert result[1].id == 2

    class TestCreateUser:
        def test_create_user(self, mocker: MockFixture):
            req = UserCreateSchema(user_name="new_user", email="new@example.com", role="user")
            mock_user = MagicMock(id=3, user_name="new_user", email="new@example.com", role="user")
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_create_user_usecase")
            mock_usecase.return_value.execute.return_value = mock_user
            result = user_handler.create_user(req, mock_usecase.return_value)
            assert result.id == 3
            assert result.user_name == "new_user"
            assert result.email == "new@example.com"
            assert result.role == "user"

    class TestUpdateUser:
        def test_update_user(self, mocker: MockFixture):
            req = UserUpdateSchema(user_name="updated_user", email="updated@example.com", role="admin")
            mock_user = MagicMock(id=1, user_name="updated_user", email="updated@example.com", role="admin")
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_update_user_usecase")
            mock_usecase.return_value.execute.return_value = mock_user
            mock_db = mocker.MagicMock()
            result = user_handler.update_user(1, req, mock_usecase.return_value, mock_db)
            assert result.id == 1
            assert result.user_name == "updated_user"
            assert result.email == "updated@example.com"
            assert result.role == "admin"

        def test_update_user_not_found(self, mocker: MockFixture):
            from app.domain.user.exceptions.user import UserNotFoundError
            from fastapi import HTTPException
            req = UserUpdateSchema(user_name="not_found", email="not_found@example.com", role="user")
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_update_user_usecase")
            mock_usecase.return_value.execute.side_effect = UserNotFoundError(999)
            mock_db = mocker.MagicMock()
            with pytest.raises(HTTPException) as exc_info:
                user_handler.update_user(999, req, mock_usecase.return_value, mock_db)
            assert exc_info.value.status_code == 404
            assert "User with ID 999 not found." in str(exc_info.value.detail)

    class TestDeleteUser:
        def test_delete_user(self, mocker: MockFixture):
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_delete_user_usecase")
            mock_usecase.return_value.execute.return_value = True
            mock_db = mocker.MagicMock()
            result = user_handler.delete_user(1, mock_usecase.return_value, mock_db)
            assert result is True

        def test_delete_user_not_found(self, mocker: MockFixture):
            from app.domain.user.exceptions.user import UserNotFoundError
            from fastapi import HTTPException
            mock_usecase = mocker.patch("app.presentation.handler.user_handler.get_delete_user_usecase")
            mock_usecase.return_value.execute.side_effect = UserNotFoundError(999)
            mock_db = mocker.MagicMock()
            with pytest.raises(HTTPException) as exc_info:
                user_handler.delete_user(999, mock_usecase.return_value, mock_db)
            assert exc_info.value.status_code == 404
            assert "User with ID 999 not found." in str(exc_info.value.detail)
