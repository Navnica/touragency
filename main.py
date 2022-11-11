import uvicorn
from routers.user import router

if __name__ == '__main__':
    uvicorn.run(router)
