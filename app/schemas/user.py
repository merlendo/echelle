from datetime import date
from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from ..models.user import UserBase


class UserCreate(UserBase):
    email: Optional[EmailStr] = None


class UserRead(UserBase):
    id: int
    created_at: Optional[date] = None


class UserUpdate(SQLModel):
    name: Optional[str] = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)
