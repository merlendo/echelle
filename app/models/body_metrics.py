from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User



class BodyMetricsBase(SQLModel):
    date: date
    weight_kg: float = Field(gt=0)
    height_cm: Optional[float] = Field(default=None, gt=0)
    neck_cm: Optional[float] = Field(default=None, gt=0)
    waist_cm: Optional[float] = Field(default=None, gt=0)
    hips_cm: Optional[float] = Field(default=None, gt=0)
    body_fat_pct: Optional[float] = Field(default=None, ge=0, le=100)
    bmi: Optional[float] = Field(default=None, gt=0)
    user_id: int


class BodyMetrics(BodyMetricsBase, table=True):
    __tablename__ = "body_metrics"

    id: Optional[int] = Field(default=None, primary_key=True)

    user: Optional["User"] = Relationship(back_populates="body_metrics")
