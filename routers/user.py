import fastapi
from resolves.user import *
from sql_base.models import User

router = fastapi.APIRouter(prefix='/user')


@router.get('/get/{user_id}', response_model=User)
def return_user(user_id: int) -> User:
    return get_user(user_id)


@router.get('/get_all')
def return_all_users() -> dict[User]:
    return get_all_users()


@router.post('/create/', response_model=User)
def create(user: User) -> User:
    return get_user(create_user(user))


@router.put("/update/{user_id}", response_model=None)
def update(user_id: int, new_data: User):
    return update_user(user_id=user_id, new_data=new_data)
