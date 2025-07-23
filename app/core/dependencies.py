from fastapi import Depends
from sqlmodel import Session

from ..models.user import User
from .database import engine


def get_session():
    with Session(engine) as session:
        yield session


def get_user(session: Session = Depends(get_session)):
    yield session.get(User, 1)
