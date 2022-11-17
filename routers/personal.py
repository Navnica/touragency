import fastapi
from sql_base.models import Personal
from resolves import personal

router = fastapi.APIRouter(prefix='/personal', tags=['Personal'])


@router.get('/get/{personal_id}', response_model=Personal | None)
def get(personal_id: int) -> Personal | None:
    return personal.get(personal_id)


@router.get('/get_all', response_model=list[Personal])
def get_all() -> list[Personal]:
    return personal.get_all()


@router.get('/remove/{personal_id}', response_model=None)
def remove(personal_id: int):
    return personal.remove(personal_id)


@router.post('/create/', response_model=Personal | dict)
def create(new_personal: Personal) -> Personal | dict:
    return personal.create(new_personal)


@router.put("/update/{personal_id}", response_model=None)
def update(personal_id: int, new_data: Personal):
    return personal.update(personal_id, new_data)

