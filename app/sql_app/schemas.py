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


class TribeCreate(TribeBase):
    pass


class Tribe(TribeBase):
    id: int
    items: list[Users] = []
    class Config:
        orm_mode = True
