from sqlmodel import Session

from ..models.body_metrics import BodyMetrics
from ..schemas.body_metrics import BodyMetricsCreate, BodyMetricsUpdate
from .base import BaseService


class BodyMetricsService(BaseService[BodyMetrics, BodyMetricsCreate, BodyMetricsUpdate]):
    def __init__(self, session: Session):
        super().__init__(BodyMetrics, session)