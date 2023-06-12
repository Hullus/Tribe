from fastapi import FastAPI
from app.routers import group, users

app = FastAPI()
app.include_router(group.router)
app.include_router(users.router)
