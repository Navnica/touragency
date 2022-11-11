from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int]


class Ticket(BaseModelModify):
    tour_id: Optional[int]
    date_start: Optional[str]
    date_end: Optional[str]
    user_id: Optional[int]


class User(BaseModelModify):
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]


class Tour(BaseModelModify):
    country_id: Optional[int]
    hours: Optional[int]
    price: Optional[float]


class Country(BaseModelModify):
    name: Optional[str]


class Personal(User):
    power_level: Optional[int]
