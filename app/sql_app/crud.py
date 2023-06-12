from sqlalchemy.orm import Session

from . import models, schemas


def get_tribe(db: Session, tribe_id: int):
    return db.query(models.Tribe).filter(models.Tribe.id == tribe_id).first()


def get_tribes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tribe).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate, tribe_id: int):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, owner_id=tribe_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
