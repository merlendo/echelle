from sqlmodel import Session

from ..models.meal_prep import MealPrep
from ..schemas.meal_prep import MealPrepCreate, MealPrepUpdate
from .base import BaseService


class MealPrepService(BaseService[MealPrep, MealPrepCreate, MealPrepUpdate]):
    def __init__(self, session: Session):
        super().__init__(MealPrep, session)
