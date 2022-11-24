import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from server.router import routers
from server.sql_base.dbmanager import DbManager

app = fastapi.FastAPI(title="taAPI",
                      version='0.1 Alpha',
                      description="taAPI - TourAgency Application Programming Interface")

[app.include_router(router) for router in routers]


@app.router.get('/', include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    DbManager('server/sql_base/touragency.db').create_db('server/sql_base/scripts/create.sql')
    uvicorn.run("start_server:app", reload=True, host='localhost')
