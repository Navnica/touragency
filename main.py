import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from router import routers
from sql_base.dbmanager import DbManager

app = fastapi.FastAPI(title="taAPI",
                      version='0.1 Alpha',
                      description="taAPI - TourAgency Application Programming Interface")
[app.include_router(router) for router in routers]


@app.router.get('/', include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    DbManager('sql_base/touragency.db').create_db('sql_base/scripts/create.sql')
    uvicorn.run("main:app", reload=True, host='localhost')
