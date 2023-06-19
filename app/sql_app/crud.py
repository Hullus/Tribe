from sqlalchemy.orm import Session

from . import models, schemas


def get_tribe(db: Session, tribe_id: int):
    return db.query(models.Tribe).filter(models.Tribe.id == tribe_id).first()


def get_tribes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tribe).offset(skip).limit(limit).all()


def create_tribe(db: Session, tribe: schemas.TribeCreate):
    db_user = models.Tribe(title=tribe.title, description=tribe.description)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Todo: should create general functions for these requests
def update_tribe(db: Session, tribe: schemas.Tribe, tribe_update: schemas.TribeUpdate):
    for field, value in tribe_update.dict(exclude_unset=True).items():
        setattr(tribe, field, value)
    db.add(tribe)
    db.commit()
    db.refresh(tribe)
    return tribe


def delete_tribe(db: Session, tribe: schemas.Tribe):
    db.delete(tribe)
    db.commit()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate, tribe_id: int):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, owner_id=tribe_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserCreate, user_update: schemas.UserUpdate):
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()
