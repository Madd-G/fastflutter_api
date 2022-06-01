from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get('/')
def fetch_users():
    return conn.execute(users.select()).fetchall()

@user.post('/create-user/')
def post_user(user: User):
    return conn.execute(users.insert().values(name=user.name, email=user.email, password=user.password))

@user.put('/update-user/{id}')
def update_user(id: int, user: User):
    return conn.execute(users.update().values(name=user.name, email=user.email, password=user.password).where(users.c.id == id))

@user.delete('/delete-user/{id}')
def delete_user(id: int):
    # c = column
    return conn.execute(users.delete().where(users.c.id == id))