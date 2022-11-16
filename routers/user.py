import fastapi
from resolves.user import *
from sql_base.models import User
from fastapi.responses import RedirectResponse

router = fastapi.APIRouter(prefix='/user')


@router.get('/get/{user_id}')
def return_user(user_id: int) -> str:
    return get_user(user_id)


@router.get('/get_all')
def return_all_users() -> str:
    return get_all_users()


@router.post('/create/')
def create(user: User) -> User:
    return create_user(user)
