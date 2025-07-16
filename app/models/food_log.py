from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class FoodLogBase(SQLModel):
    timestamp: datetime
    description: str
    quantity_g: Optional[float] = Field(default=None, gt=0)
    calories_kcal: Optional[float] = Field(default=None, gt=0)
    protein_g: Optional[float] = Field(default=None, ge=0)
    carbs_g: Optional[float] = Field(default=None, ge=0)
    fat_g: Optional[float] = Field(default=None, ge=0)
    user_id: int


class FoodLog(FoodLogBase, table=True):
    __tablename__ = "food_log"

    id: Optional[int] = Field(default=None, primary_key=True)

    user: Optional["User"] = Relationship(back_populates="food_logs")
