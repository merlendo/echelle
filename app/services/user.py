from sqlmodel import Session

from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from .base import BaseService


class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, session: Session):
        super().__init__(User, session)
