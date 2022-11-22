import fastapi
from resolves import user
from sql_base.models import User

router = fastapi.APIRouter(prefix='/user', tags=['User'])


@router.get('/get/{user_id}', response_model=User | None)
def get(user_id: int) -> User | None:
    return user.get(user_id)


@router.get('/get_all', response_model=list[User] | dict)
def get_all() -> list[User] | dict:
    return user.get_all()


@router.get('/remove/{user_id}', response_model=None)
def remove(user_id: int) -> None:
    return user.remove(user_id)


@router.post('/create/', response_model=User | dict)
def create(new_user: User) -> User | dict:
    return user.create(new_user)


@router.put("/update/{user_id}", response_model=None)
def update(user_id: int, new_data: User):
    return user.update(user_id=user_id, new_data=new_data)
