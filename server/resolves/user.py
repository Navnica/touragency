from sql_base.dbmanager import DbManager
from sql_base.models import User

dbmanager = DbManager(db_path='sql_base/touragency.db')


def get(user_id: int) -> User | None:
    res = dbmanager.execute_query(query='select * from User where id=(?)', args=(user_id,))

    return None if not res else User(
        id=res[0],
        name=res[1],
        surname=res[2],
        phone=res[3]
    )


def get_all() -> list[User] | dict:
    user_list = dbmanager.execute_query(query="select * from User", fetchone=False)

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
    return dbmanager.execute_query('delete from User where id=(?)', args=(user_id,))


def create(new_user: User) -> int | dict:
    res = dbmanager.execute_query(
        query="insert into User (name, surname, phone) values(?,?,?) returning id",
        args=(new_user.name, new_user.surname, new_user.phone))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(user_id: int, new_data: User) -> None:
    return dbmanager.execute_query(
        query='update User set (name, surname, phone) = (?,?,?) where id=(?)',
        args=(new_data.name, new_data.surname, new_data.phone, user_id))


def login(user: User) -> User:
    pass