import requests
from server.sql_base.models import User


def server_available() -> bool | dict:
    try:
        requests.get(url='http://localhost:8000/')

    except requests.exceptions.ConnectionError:
        return {'error': 'server not available'}

    return True


def login(user_login: str, user_password: str) -> dict | None:
    conn_a = server_available()

    if 'error' in conn_a:
        return conn_a

    answer = requests.post(
        url='http://localhost:8000/user/login',
        data=f'{{ "phone": "{user_login}", "password": "{user_password}" }}').json()

    return answer


def register(user: User) -> dict | int:
    conn_a = server_available()

    if 'error' in conn_a:
        return conn_a

    data = f'{{"name": "{user.name}", "surname": "{user.surname}", "phone": "{user.phone}", "password": "{user.password}"}}'

    answer = requests.post(
        url='http://localhost:8000/user/create',
        data=data).json()

    return answer

