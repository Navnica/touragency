from sql_base.models import Personal
from .user import dbmanager


def get(personal_id: int) -> Personal | None:
    res = dbmanager.execute_query(
        query='select * from Personal where id=(?)',
        args=(personal_id,))

    return None if not res else Personal(
        id=res[0],
        name=res[1],
        surname=res[2],
        phone=res[3],
        power_level=res[4]
    )


def get_all() -> list[Personal] | dict:
    personal_list = dbmanager.execute_query(
        query="select * from Personal",
        fetchone=False)

    res = []

    if personal_list:
        for user in personal_list:
            res.append(Personal(
                id=user[0],
                name=user[1],
                surname=user[2],
                phone=user[3],
                power_level=user[4]
            ))

    return res


def remove(personal_id: int) -> None:
    return dbmanager.execute_query(
        query='delete from Personal where id=(?)',
        args=(personal_id,))


def create(new_personal: Personal) -> int | dict:
    res = dbmanager.execute_query(
        query="insert into Personal (name, surname, phone, power_level) values(?,?,?,?) returning id",
        args=(new_personal.name, new_personal.surname, new_personal.phone, new_personal.power_level))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(personal_id: int, new_data: Personal) -> None:
    return dbmanager.execute_query(
        query=f"update Personal set (name, surname, phone, power_level) = (?,?,?,?) where id=(?)",
        args=(new_data.name, new_data.surname, new_data.phone, new_data.power_level, personal_id))

