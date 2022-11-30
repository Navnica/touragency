import requests
from server.sql_base.models import User


def login(user_login: str, user_password: str) -> dict | None:
    answer = requests.post(
        url='http://localhost:8000/user/login',
        data=f'{{ "phone": "{user_login}", "password": "{user_password}" }}').json()

    return answer


def register(user: User) -> dict:
    data = f'{{"name": "{user.name}", "surname": "{user.surname}", "phone": "{user.phone}", "password": "{user.password}"}}'
    answer = requests.post(
        url='http://localhost:8000/user/create',
        data=data).json()

    return answer
