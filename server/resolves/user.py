from server.sql_base.dbmanager import DbManager
from server.sql_base.models import User

dbmanager = DbManager(db_path='server/sql_base/touragency.db')


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
        query="insert into User (name, surname, phone, password) values(?,?,?,?) returning id",
        args=(new_user.name, new_user.surname, new_user.phone, new_user.password))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(user_id: int, new_data: User) -> None:
    return dbmanager.execute_query(
        query='update User set (name, surname, phone) = (?,?,?) where id=(?)',
        args=(new_data.name, new_data.surname, new_data.phone, user_id))


def login(user_phone: str, user_password: str) -> int | None:
    res = dbmanager.execute_query(
        query='select id from User where phone=(?) and password=(?) ',
        args=(user_phone, user_password)
    )

    return get(res[0]) if res else None

