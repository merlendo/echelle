from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from ..models.exercise_log import ExerciseLogBase


class ExerciseLogCreate(ExerciseLogBase):
    pass


class ExerciseLogRead(ExerciseLogBase):
    id: int


class ExerciseLogUpdate(SQLModel):
    timestamp: Optional[datetime] = None
    exercise_type: Optional[str] = None
    duration_min: Optional[float] = Field(default=None, gt=0)
    calories_burned_kcal: Optional[float] = Field(default=None, gt=0)
    notes: Optional[str] = None
    user_id: Optional[int] = None
