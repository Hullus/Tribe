from fastapi import FastAPI
from app.routers import group, user

from app.sql_app import models
from app.sql_app.database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(group.router)
app.include_router(user.router)
