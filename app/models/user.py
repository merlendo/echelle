from datetime import date
from enum import Enum
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .body_metrics import BodyMetrics
    from .exercise_log import ExerciseLog
    from .food_log import FoodLog
    from .meal_prep import MealPrep
    from .photo_log import PhotoLog


class Sex(str, Enum):
    male = "male"
    female = "female"


class UserBase(SQLModel):
    username: str
    first_name: str
    last_name: str
    email: str
    sex: Sex


class User(UserBase, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[date] = Field(default_factory=date.today)

    body_metrics: List["BodyMetrics"] = Relationship(back_populates="user")
    food_logs: List["FoodLog"] = Relationship(back_populates="user")
    exercise_logs: List["ExerciseLog"] = Relationship(back_populates="user")
    meal_preps: List["MealPrep"] = Relationship(back_populates="user")
    photo_logs: List["PhotoLog"] = Relationship(back_populates="user")
