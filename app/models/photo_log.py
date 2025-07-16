from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class PhotoLogBase(SQLModel):
    date: date
    photo_path: str
    description: Optional[str] = None
    user_id: int


class PhotoLog(PhotoLogBase, table=True):
    __tablename__ = "photo_log"

    id: Optional[int] = Field(default=None, primary_key=True)

    user: Optional["User"] = Relationship(back_populates="photo_logs")
