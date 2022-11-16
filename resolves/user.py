from sql_base.dbmanager import DbManager
from sql_base.models import User
from typing import Optional


def get_user(user_id: int) -> User:
    return DbManager(
        db_path='sql_base/touragency.db').execute_query(
        f'select * from User where id={user_id}'
    )


def get_all_users() -> str:
    return DbManager(
        db_path='sql_base/touragency.db').execute_query(
        query="select * from User")


def create_user(user: User) -> Optional[User]:
    return DbManager(db_path='sql_base/touragency.db').execute_query(
        query="insert into User (name, surname, phone) values(?,?,?) returning id",
        insert=True,
        args=(user.name, user.surname, user.phone))
