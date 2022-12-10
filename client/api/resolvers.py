import requests
from server.sql_base.models import User
import settings

server_url = f'http://{settings.SERVER_HOST}:{settings.SERVER_PORT}'


def server_available() -> bool | dict:
    try:
        requests.get(url=server_url)

    except requests.exceptions.ConnectionError:
        return {'error': 'Server not available'}

    return True


def login(user_login: str, user_password: str) -> dict | None:
    conn_a = server_available()

    if type(conn_a) is dict:
        return conn_a

    answer = requests.post(
        url=f'{server_url}/user/login',
        data=f'{{ "phone": "{user_login}", "password": "{user_password}" }}').json()

    return answer


def register(user: User) -> dict | int:
    conn_a = server_available()

    if type(conn_a) is dict:
        return conn_a

    data = f'{{"name": "{user.name}", "surname": "{user.surname}", "phone": "{user.phone}", "password": "{user.password}"}}'

    answer = requests.post(
        url=f'{server_url}/user/create',
        data=data).json()

    return answer


def update(user: User) -> None | dict:
    conn_a = server_available()

    if type(conn_a) is dict:
        return conn_a
