from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from ..models.food_log import FoodLogBase


class FoodLogCreate(FoodLogBase):
    pass


class FoodLogRead(FoodLogBase):
    id: int


class FoodLogUpdate(SQLModel):
    timestamp: Optional[datetime] = None
    description: Optional[str] = None
    quantity_g: Optional[float] = Field(default=None, gt=0)
    calories_kcal: Optional[float] = Field(default=None, gt=0)
    protein_g: Optional[float] = Field(default=None, ge=0)
    carbs_g: Optional[float] = Field(default=None, ge=0)
    fat_g: Optional[float] = Field(default=None, ge=0)
    user_id: Optional[int] = None
