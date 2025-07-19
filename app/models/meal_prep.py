from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class MealPrepBase(SQLModel):
    date: date
    meal_name: str
    description: Optional[str] = None
    calories_kcal: Optional[float] = Field(default=None, gt=0)
    protein_g: Optional[float] = Field(default=None, ge=0)
    carbs_g: Optional[float] = Field(default=None, ge=0)
    fat_g: Optional[float] = Field(default=None, ge=0)
    user_id: int = Field(foreign_key="user.id")


class MealPrep(MealPrepBase, table=True):
    __tablename__ = "meal_prep"

    id: Optional[int] = Field(default=None, primary_key=True)

    user: Optional["User"] = Relationship(back_populates="meal_preps")
