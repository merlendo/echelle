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


class BodyMetrics(BodyMetricsBase, table=True):
    __tablename__ = "body_metrics"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="body_metrics")

    @property
    def bmi(self) -> Optional[float]:
        if self.weight_kg and self.height_cm:
            return round(10000 * self.weight_kg / (self.height_cm**2), 2)
        return None

    @property
    def bodyfat(self) -> Optional[float]:
        if not self.user or not self.user.sex:
            return None
        sex = self.user.sex
        if sex == "male" and self.waist_cm and self.neck_cm and self.height_cm:
            return round(
                495
                / (
                    1.0324
                    - 0.19077 * (self.waist_cm - self.neck_cm)
                    + 0.15456 * self.height_cm
                )
                - 450,
                2,
            )
        elif (
            sex == "female"
            and self.waist_cm
            and self.hips_cm
            and self.neck_cm
            and self.height_cm
        ):
            return round(
                495
                / (
                    1.29579
                    - 0.35004 * (self.waist_cm + self.hips_cm - self.neck_cm)
                    + 0.22100 * self.height_cm
                )
                - 450,
                2,
            )
        return None
