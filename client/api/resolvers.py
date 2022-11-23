import requests


def login(user_login: str, user_password: str):
    answer = requests.post(
        url='http://localhost:8000/userin/login',
        data=f'{{ "login": "{user_login}", "password": "{user_password}" }}').json()

    return answer
