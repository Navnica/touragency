from sql_base.dbmanager import DbManager
from sql_base.models import User


def get_user(user_id: int) -> User:
    return DbManager(
        db_path='sql_base/touragency.db').execute_query(
        f'select * from User where id={user_id}'
    )


def get_all_users() -> dict[User]:
    return DbManager(
        db_path='sql_base/touragency.db').execute_query(
        query="select * from User")


def create_user(user: User) -> int:
    return DbManager(db_path='sql_base/touragency.db').execute_query(
        query="insert into User (name, surname, phone) values(?,?,?) returning id",
        insert=True,
        args=(user.name, user.surname, user.phone))


def update_user(user_id: int, new_data: User) -> User:
    return DbManager(db_path='sql_base/touragency.db').execute_query(
        query=f"update User set (name, surname, phone) = ('{new_data.name}', '{new_data.surname}', '{new_data.phone}') where id={user_id}")
