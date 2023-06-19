from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.group import get_db
from app.sql_app import schemas
from app.sql_app.crud import create_user, get_users, get_user, update_user, delete_user
from app.sql_app.models import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{id}")
async def read_user_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{tribe_id}", response_model=schemas.User)
async def create_tribe_member(tribe_id, user: schemas.UserCreate, db: Session = Depends(get_db)):
    response = create_user(db, user, tribe_id)
    return response


@router.put("/{user_id}", response_model=schemas.User)
async def update_user_data(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    existing_user = get_user(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = update_user(db, existing_user, user)
    return updated_user


@router.delete("/{user_id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = get_user(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    delete_user(db, existing_user)
    return {"message": "User deleted successfully"}

@router.get("/me")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]
