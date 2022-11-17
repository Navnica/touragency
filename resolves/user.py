from sql_base.dbmanager import DbManager
from sql_base.models import User


def get(user_id: int) -> User | None:
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


def get_all() -> list[User] | dict:
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

    return res


def remove(user_id: int) -> None:
    return DbManager(
        db_path='sql_base/touragency.db').execute_query(
        f'delete from User where id={user_id}'
    )


def create(new_user: User) -> int | dict:
    res = DbManager(db_path='sql_base/touragency.db').execute_query(
        query="insert into User (name, surname, phone) values(?,?,?) returning id",
        insert=True,
        args=(new_user.name, new_user.surname, new_user.phone))

    if type(res) != dict:
        res = get(res)

    return res


def update(user_id: int, new_data: User) -> None:
    return DbManager(db_path='sql_base/touragency.db').execute_query(
        query=f"update User set (name, surname, phone) = ('{new_data.name}', '{new_data.surname}', '{new_data.phone}') where id={user_id}")


