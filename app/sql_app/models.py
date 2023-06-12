from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Tribe(Base):
    __tablename__ = "tribe"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # special_habits = Column(set, )
    items = relationship("Users", back_populates="owner")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    owner_id = Column(Integer, ForeignKey("tribe.id"))

    owner = relationship("Tribe", back_populates="users")  # Note important attribute TODO: research this and add habits
