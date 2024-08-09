from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    nome: str
    CPF: str
    dataNascimento: str
    email: EmailStr
    UF: str
    


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    nome: str
    dataNascimento: str
    email: EmailStr
    UF: str
    


class UserList(BaseModel):
    users: list[UserPublic]
