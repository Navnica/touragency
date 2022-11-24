import fastapi
from server.sql_base.models import UserIn
from server.resolves import userin

router = fastapi.APIRouter(prefix='/userin', tags=['UserIn'], include_in_schema=False)


@router.post('/login')
def login(userIn: UserIn) -> UserIn | None:
    return userin.login(userIn)


@router.post('/register')
def register(userIn: UserIn) -> None | dict:
    return userin.register(userIn)
