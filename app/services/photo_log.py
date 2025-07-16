from sqlmodel import Session

from ..models.photo_log import PhotoLog
from ..schemas.photo_log import PhotoLogCreate, PhotoLogUpdate
from .base import BaseService


class PhotoLogService(BaseService[PhotoLog, PhotoLogCreate, PhotoLogUpdate]):
    def __init__(self, session: Session):
        super().__init__(PhotoLog, session)
