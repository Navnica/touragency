from .user import dbmanager
from sql_base.models import UserIn


def login(user_login: str, user_password: str) -> UserIn | None:
    user = dbmanager.execute_query(
        query='select userId from UserIn where login = (?) and password = (?)',
        fetchone=True,
        args=(user_login, user_password))

    print(user)