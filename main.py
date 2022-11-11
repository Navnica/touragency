import uvicorn
import fastapi
from routers.user import router as user_router

app = fastapi.FastAPI()


if __name__ == '__main__':
    app.include_router(user_router)
    uvicorn.run(app)
