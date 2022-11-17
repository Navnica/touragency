from sql_base.dbmanager import DbManager
from sql_base.models import User


def get_user(user_id: int) -> User | None:
    res = DbManager(
        db_path='sql_base/touragency.db').execute_query(
        f'select * from User where id={user_id}'
    )

    return None if not res else User(
        id=res[0][0],
        name=res[0][1],
        surname=res[0][2],
        phone=res[0][3]
    )


def get_all_users() -> list[User] | None:
    user_list = DbManager(
        db_path='sql_base/touragency.db').execute_query(
        query="select * from User")

    res = []

    if user_list:
        for user in user_list:
            res.append(User(
                id=user[0],
                name=user[1],
                surname=user[2],
                phone=user[3]
            ))
    else:
        res = None

    return res


def create_user(user: User) -> int | dict:
    return DbManager(db_path='sql_base/touragency.db').execute_query(
        query="insert into User (name, surname, phone) values(?,?,?) returning id",
        insert=True,
        args=(user.name, user.surname, user.phone))


def update_user(user_id: int, new_data: User) -> User:
    return DbManager(db_path='sql_base/touragency.db').execute_query(
        query=f"update User set (name, surname, phone) = ('{new_data.name}', '{new_data.surname}', '{new_data.phone}') where id={user_id}")


def delete_user(user_id: int) -> None:
    return DbManager(
        db_path='sql_base/touragency.db').execute_query(
        f'delete from User where id={user_id}'
    )