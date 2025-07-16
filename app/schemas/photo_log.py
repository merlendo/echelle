from datetime import date as Date
from typing import Optional

from sqlmodel import SQLModel

from ..models.photo_log import PhotoLogBase


class PhotoLogCreate(PhotoLogBase):
    pass


class PhotoLogRead(PhotoLogBase):
    id: int


class PhotoLogUpdate(SQLModel):
    date: Optional[Date] = None
    photo_path: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
