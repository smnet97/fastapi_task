from fastapi import FastAPI

from app.auth.base_config import fastapi_users, auth_backend
from app.auth.schemas import UserRead, UserCreate
from app.auth.router import router as auth_router

app = FastAPI(
    title='project 1'
)


@app.get("/")
def get_info():
    return {
        "status": "success",
        "details": "Hello, Alex!"
    }


current_user = fastapi_users.current_user()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(auth_router)
