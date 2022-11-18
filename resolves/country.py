from sql_base.models import Country
from sql_base.dbmanager import DbManager
from .user import dbmanager


def get(country_id: int) -> Country | None:
    res = dbmanager.execute_query(f'select * from Country where id={country_id}')

    return None if not res else Country(
        id=res[0][0],
        name=res[0][1]
    )


def get_all() -> list[Country] | dict:
    country_list = dbmanager.execute_query(query="select * from Country")

    res = []

    if country_list:
        for user in country_list:
            res.append(Country(
                id=user[0],
                name=user[1],
            ))

    return res


def remove(country_id: int) -> None:
    return dbmanager.execute_query(f'delete from Country where id={country_id}')


def create(new_country: Country) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into Country (name) values('{new_country.name}') returning id",)[0][0]

    if type(res) != dict:
        res = get(res)

    return res

def update(country_id: int, new_data: Country) -> None:
    return dbmanager.execute_query(
        query=f"update Country set (name) = ('{new_data.name}') where id={country_id}")

