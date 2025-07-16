from datetime import date as Date
from typing import Optional

from sqlmodel import Field, SQLModel

from ..models.meal_prep import MealPrepBase


class MealPrepCreate(MealPrepBase):
    pass


class MealPrepRead(MealPrepBase):
    id: int


class MealPrepUpdate(SQLModel):
    date: Optional[Date] = None
    meal_name: Optional[str] = None
    description: Optional[str] = None
    calories_kcal: Optional[float] = Field(default=None, gt=0)
    protein_g: Optional[float] = Field(default=None, ge=0)
    carbs_g: Optional[float] = Field(default=None, ge=0)
    fat_g: Optional[float] = Field(default=None, ge=0)
    user_id: Optional[int] = None
