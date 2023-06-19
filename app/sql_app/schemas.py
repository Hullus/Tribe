# import uuid

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: str = Field(None, title="Email")
    hashed_password: str = Field(None, title="Hashed Password")
    is_active: bool = Field(None, title="Is Active")


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


class TribeUpdate(BaseModel):
    title: str = Field(None, title="Title")
    description: str = Field(None, title="Description")


class Tribe(TribeBase):
    id: int

    class Config:
        orm_mode = True
