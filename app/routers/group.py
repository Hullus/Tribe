from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.sql_app import schemas
from app.sql_app.crud import get_tribes, get_tribe, create_tribe
from app.sql_app.database import SessionLocal

router = APIRouter(
    prefix="/group",
    tags=["group"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/",)
async def read_tribe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = get_tribes(db, skip=skip, limit=limit)
    return groups


@router.get("/{id}")
async def read_tribe_by_id(id: int, db: Session = Depends(get_db)):
    tribe = get_tribe(db, id)
    if tribe is None:
        raise HTTPException(status_code=404, detail="User not found")

    return tribe


@router.post("/", response_model=schemas.Tribe)
async def read_group(Tribe: schemas.TribeCreate, db: Session = Depends(get_db)):
    response = create_tribe(db, Tribe)
    return response

@router.put("/")
async def read_group():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/")
async def read_group():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_group_me():
    return {"username": "fakecurrentuser"}



