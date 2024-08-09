from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Message, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )
        elif db_user.cpf == user.cpf:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='CPF already exists',
            )

    db_user = User(
        username=user.username, email=user.email, cpf=user.cpf, uf=user.uf
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@app.get("/users/{cpf}/", response_model=UserPublic)
def get_user_by_cpf(cpf: str, db: Session = Depends(get_session)):
    user = db.query(User).filter_by(cpf=cpf).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


@app.put("/users/{cpf}/", response_model=UserPublic)
def update_user(cpf: str, user: UserSchema, db: Session = Depends(get_session)):
    existing_user = db.query(User).filter_by(cpf=cpf).first()
    
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.username:
        existing_user.username = user.username
    if user.email:
        existing_user.email = user.email
    if user.uf:
        existing_user.uf = user.uf

    db.commit()
    db.refresh(existing_user)
    return existing_user


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}
