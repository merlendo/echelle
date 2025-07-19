from typing import Optional

from fastapi import HTTPException, status
from sqlmodel import Session

from ..models.body_metrics import BodyMetrics
from ..schemas.body_metrics import BodyMetricsCreate, BodyMetricsUpdate
from .base import BaseService


class BodyMetricsService(
    BaseService[BodyMetrics, BodyMetricsCreate, BodyMetricsUpdate]
):
    def __init__(self, session: Session):
        super().__init__(BodyMetrics, session)

    def get_bmi(self, metric_id: int) -> Optional[float]:
        obj = self.session.get(self.model, metric_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} with ID {metric_id} not found.",
            )
        return obj.bmi

    def get_bodyfat(self, metric_id: int) -> Optional[float]:
        obj = self.session.get(self.model, metric_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} with ID {metric_id} not found.",
            )
        return obj.bodyfat
