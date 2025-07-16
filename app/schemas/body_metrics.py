from datetime import date as Date
from typing import Optional

from sqlmodel import Field, SQLModel

from ..models.body_metrics import BodyMetricsBase


class BodyMetricsCreate(BodyMetricsBase):
    pass


class BodyMetricsRead(BodyMetricsBase):
    id: int


class BodyMetricsUpdate(SQLModel):
    date: Optional[Date] = None
    weight_kg: Optional[float] = Field(default=None, gt=0)
    height_cm: Optional[float] = Field(default=None, gt=0)
    neck_cm: Optional[float] = Field(default=None, gt=0)
    waist_cm: Optional[float] = Field(default=None, gt=0)
    hips_cm: Optional[float] = Field(default=None, gt=0)
    body_fat_pct: Optional[float] = Field(default=None, ge=0, le=100)
    bmi: Optional[float] = Field(default=None, gt=0)
    user_id: Optional[int] = None
