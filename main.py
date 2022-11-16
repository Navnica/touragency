import uvicorn
import fastapi
from routers.user import router as user_router
from sql_base.dbmanager import DbManager

app = fastapi.FastAPI()


if __name__ == '__main__':
    DbManager('sql_base/touragency.db').create_db('sql_base/scripts/create.sql')
    app.include_router(user_router)
    uvicorn.run(app)
