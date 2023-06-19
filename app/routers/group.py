from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.sql_app import schemas
from app.sql_app.crud import get_tribes, get_tribe, create_tribe, delete_tribe
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


@router.get("/", )
async def read_tribe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = get_tribes(db, skip=skip, limit=limit)
    return groups


@router.get("/{tribe_id}")
async def read_tribe_by_id(tribe_id: int, db: Session = Depends(get_db)):
    tribe = get_tribe(db, tribe_id)
    if tribe is None:
        raise HTTPException(status_code=404, detail="Tribe not found")

    return tribe


@router.post("/", response_model=schemas.Tribe)
async def read_group(tribe: schemas.TribeCreate, db: Session = Depends(get_db)):
    response = create_tribe(db, tribe)
    return response


@router.put("/{tribe_id}", response_model=schemas.Tribe)
async def update_tribe_data(tribe_id: int, tribe: schemas.TribeUpdate, db: Session = Depends(get_db)):
    existing_tribe = get_tribe(db, tribe_id)
    if existing_tribe is None:
        raise HTTPException(status_code=404, detail="Tribe not found")

    updated_tribe = update_tribe(db, existing_tribe, tribe)
    return updated_tribe

@router.delete("/{tribe_id}")
async def remove_tribe(tribe_id: int, db: Session = Depends(get_db)):
    existing_tribe = get_tribe(db, tribe_id)
    if existing_tribe is None:
        raise HTTPException(status_code=404, detail="Tribe not found")

    delete_tribe(db, existing_tribe)
    return {"message": "Tribe deleted successfully"}

@router.get("/me")
async def read_group_me():
    return {"username": "fakecurrentuser"}
