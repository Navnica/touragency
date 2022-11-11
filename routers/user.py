import fastapi
from resolves.user import get_user

router = fastapi.APIRouter()


@router.route('/users/get/{user_id}')
def return_user(user_id: int) -> str:
    return get_user(user_id)
