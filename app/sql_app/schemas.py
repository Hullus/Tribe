# import uuid

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    owner_id: int

    class Config:
        orm_mode = True


class TribeBase(BaseModel):
    title: str
    description: str
    Members: list[User] = []


class TribeCreate(TribeBase):
    pass


class Tribe(TribeBase):
    id: int

    class Config:
        orm_mode = True
