import client.api.resolvers
from server.sql_base.models import User


class Session:
    auth: bool = False
    user: User = User(
        name=None,
        surname=None,
        phone=None,
        pasword=None,
        power_level=0
    )
    error = None

    def login(self, user_login, user_password) -> None:
        answer: User | dict = client.api.resolvers.login(user_login, user_password)

        match answer:
            case {'error': error}:
                self.error = error

            case {'id': _}:
                self.user = User(
                    id=answer['id'],
                    name=answer['name'],
                    surname=answer['surname'],
                    phone=answer['phone'],
                    password=user_password,
                    power_level=answer['power_level']
                )
                self.auth = True

    def register(self, user: User):
        answer: User | dict = client.api.resolvers.register(user)

        match answer:
            case {'error': error}:
                self.error = error

            case {'id': _}:
                self.auth = True
