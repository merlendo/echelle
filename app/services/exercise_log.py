from sqlmodel import Session

from ..models.exercise_log import ExerciseLog
from ..schemas.exercise_log import ExerciseLogCreate, ExerciseLogUpdate
from .base import BaseService


class ExerciseLogService(BaseService[ExerciseLog, ExerciseLogCreate, ExerciseLogUpdate]):
    def __init__(self, session: Session):
        super().__init__(ExerciseLog, session)
