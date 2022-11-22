import fastapi
from sql_base.models import UserIn
from resolves import userin

router = fastapi.APIRouter(prefix='/userin', tags=['UserIn'])


@router.post('/login')
def login(userIn: UserIn) -> UserIn | None:
    userin.login(userIn)

