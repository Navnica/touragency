import pydentic.exceptions
import typing
import fastapi
from resolves import ticket
from sql_base.models import Ticket

router = fastapi.APIRouter(prefix='/ticket', tags=['Ticket'])


@router.get('/get/{ticket_id}', response_model=Ticket | None)
def get(ticket_id: int) -> Ticket | None:
    return ticket.get(ticket_id)


@router.get('/get_all', response_model=list[Ticket] | dict)
def get_all() -> list[Ticket] | dict:
    return ticket.get_all()


@router.get('/remove/{ticket_id}', response_model=None)
def remove(ticket_id: int) -> None:
    return ticket.remove(ticket_id)


@router.post('/create/', response_model=Ticket | dict)
def create(new_ticket: Ticket) -> Ticket | dict:
    return ticket.create(new_ticket)


@router.put("/update/{ticket_id}", response_model=None)
def update(ticket_id: int, new_data: Ticket):
    return ticket.update(ticket_id=ticket_id, new_data=new_data)
