import fastapi
from resolves.user import *
from sql_base.models import User

router = fastapi.APIRouter(prefix='/user')


@router.get('/get/{user_id}', response_model=User | None)
def return_user(user_id: int) -> User | None:
    return get_user(user_id)


@router.get('/get_all', response_model=list[User])
def return_all_users() -> list[User]:
    return get_all_users()


@router.post('/create/', response_model=User | dict)
def create(user: User) -> User | dict:
    res = create_user(user)

    if type(res) == dict:
        return res
    else:
        return get_user(res)


@router.put("/update/{user_id}", response_model=None)
def update(user_id: int, new_data: User):
    return update_user(user_id=user_id, new_data=new_data)


@router.get('/remove/{user_id}', response_model=None)
def remove(user_id: int):
    return delete_user(user_id)