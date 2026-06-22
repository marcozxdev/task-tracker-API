from fastapi import FastAPI

from src.routes.user import router as user_router

from src.routes.tasks import router as task_router


app = FastAPI()


app.include_router(

    user_router,

    prefix="/users",

    tags=["Users"]

)


app.include_router(

    task_router,

    prefix="/tasks",

    tags=["Tasks"]

)