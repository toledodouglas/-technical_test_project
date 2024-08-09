from pydantic import BaseModel, ConfigDict, EmailStr

from pydantic_br import CPFDigits


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    cpf: CPFDigits
    email: EmailStr
    uf: str
    dataNasc: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)
    uf: str
    dataNasc: str


class UserList(BaseModel):
    users: list[UserPublic]
