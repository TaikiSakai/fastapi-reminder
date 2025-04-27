from pydantic import BaseModel, Field

from app.domain.user.entities import User


class UserSchema(BaseModel):
    id: int | None
    user_name: str
    email: str
    role: str

    @staticmethod
    def from_entity(user: User) -> 'UserSchema':
        return UserSchema(
            id=user.id,
            user_name=str(user.user_name),
            email=str(user.email),
            role=user.role
        )


class UserCreateSchema(BaseModel):
    user_name: str = Field(min_length=1, max_length=100)
    email: str
    role: str   


class UserUpdateSchema(BaseModel):
    user_name: str | None = Field(min_length=1, max_length=100)
    email: str | None
    role: str | None


class UserResponeSchema(BaseModel):
    id: int
    user_name: str
    email: str

    class Config:
        orm_mode = True
