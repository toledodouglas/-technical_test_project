from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    senha: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
