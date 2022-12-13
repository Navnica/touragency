from typing import Callable, Tuple, Any, Dict

import requests
from server.sql_base import models
import settings

server_url = f'http://{settings.SERVER_HOST}:{settings.SERVER_PORT}'


def server_available(func) -> Callable[[tuple[Any, ...], dict[str, Any]], dict[str, str] | Any]:
    def need_it(*args, **kwargs):
        try:
            requests.get(url=server_url)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {'error': 'Server not available'}

    return need_it


@server_available
def login(user_login: str, user_password: str) -> dict | None:
    answer = requests.post(
        url=f'{server_url}/user/login',
        data=f'{{ "phone": "{user_login}", "password": "{user_password}" }}').json()

    return answer


@server_available
def register(user: models.User) -> dict | int:
    data = f'{{"name": "{user.name}", "surname": "{user.surname}", "phone": "{user.phone}", "password": "{user.password}"}}'

    answer = requests.post(
        url=f'{server_url}/user/create',
        data=data).json()

    return answer


@server_available
def update_user(user: models.User) -> None | dict:
    data = f'{{"name": "{user.name}", "surname": "{user.surname}", "phone": "{user.phone}", "password": "{user.password}"}}'

    answer = requests.put(
        url=f'{server_url}/user/update/{user.id}',
        data=data).json()

    return answer


@server_available
def get_all_tours() -> dict:
    return requests.get(url=f'{server_url}/tour/get_all').json()


@server_available
def get_country_by_id(country_id: int):
    return requests.get(url=f'{server_url}/country/get/{country_id}').json()
