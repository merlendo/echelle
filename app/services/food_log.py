from sqlmodel import Session

from ..models.food_log import FoodLog
from ..schemas.food_log import FoodLogCreate, FoodLogUpdate
from .base import BaseService


class FoodLogService(BaseService[FoodLog, FoodLogCreate, FoodLogUpdate]):
    def __init__(self, session: Session):
        super().__init__(FoodLog, session)
