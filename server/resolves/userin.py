from .user import dbmanager
from sql_base.models import UserIn


def login(userIn: UserIn) -> int | None:
    user = dbmanager.execute_query(
        query='select userId from UserIn where login = (?) and password = (?)',
        fetchone=True,
        args=(userIn.login, userIn.password))

    return None if not user else int(user[0])


def register(userIn: UserIn) -> None | dict:
    new_user = dbmanager.execute_query(
        query='insert into UserIn(login, password, userId) values(?, ?, ?)',
        fetchone=True,
        args=(userIn.login, userIn.password, userIn.user_id)
    )

    return new_user if type(new_user) == dict else None
