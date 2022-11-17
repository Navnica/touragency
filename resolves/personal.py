from sql_base.models import Personal
from sql_base.dbmanager import DbManager


def get(personal_id: int) -> Personal | None:
    pass


def get_all() -> list[Personal] | dict:
    pass


def remove(personal_id: int) -> None:
    pass


def create(new_personal: Personal) -> int | dict:
    pass


def update(personal_id: int, new_data: Personal) -> None:
    pass
