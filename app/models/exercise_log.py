from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class ExerciseLogBase(SQLModel):
    timestamp: datetime
    exercise_type: str
    duration_min: Optional[float] = Field(default=None, gt=0)  # durée en minutes
    calories_burned_kcal: Optional[float] = Field(default=None, gt=0)
    notes: Optional[str] = None
    user_id: int = Field(foreign_key="user.id")


class ExerciseLog(ExerciseLogBase, table=True):
    __tablename__ = "exercise_log"

    id: Optional[int] = Field(default=None, primary_key=True)

    user: Optional["User"] = Relationship(back_populates="exercise_logs")
