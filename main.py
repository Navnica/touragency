import uvicorn
import fastapi
from router import routers
from sql_base.dbmanager import DbManager

app = fastapi.FastAPI(title="TouragencyAPI", version='0.1 Alpha', )
[app.include_router(router) for router in routers]

if __name__ == '__main__':
    DbManager('sql_base/touragency.db').create_db('sql_base/scripts/create.sql')
    uvicorn.run("main:app", reload=True)
