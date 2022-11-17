from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None


class Ticket(BaseModelModify):
    tour_id: int
    date_start: str
    date_end: str
    user_id: int


class User(BaseModelModify):
    name: str
    surname: str
    phone: str


class Tour(BaseModelModify):
    country_id: int
    hours: int
    price: float


class Country(BaseModelModify):
    name: str


class Personal(User):
    power_level: int
