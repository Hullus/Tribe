from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.routers.group import get_db
from app.sql_app import schemas
from app.sql_app.crud import create_user
from app.sql_app.models import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/{tribe_id}", response_model=schemas.User)
async def create_tribe_member(tribe_id,  user: schemas.UserCreate, db: Session = Depends(get_db)):
    response = create_user(db, user, tribe_id)
    return response

@router.put("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{id}")
async def read_user_by_id():
    return [{"username": "Rick"}, {"username": "Morty"}]
