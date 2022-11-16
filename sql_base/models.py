from pydantic import BaseModel
from typing import Optional
from fastapi import Query


class BaseModelModify(BaseModel):
    id: Optional[int]


class Ticket(BaseModelModify):
    tour_id: int
    date_start: str
    date_end: str
    user_id: int


class User(BaseModel):
    name: Optional[str]
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
