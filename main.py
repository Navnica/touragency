import uvicorn
import fastapi
from routers.user import router as user_router
from sql_base.dbmanager import DbManager

app = fastapi.FastAPI()
app.include_router(user_router, prefix=user_router.prefix)

if __name__ == '__main__':
    DbManager('sql_base/touragency.db').create_db('sql_base/scripts/create.sql')
    uvicorn.run("main:app", reload=True)
