from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session
from ...schemas.user import UserCreate, UserRead, UserUpdate
from ...services.user import UserService

router = APIRouter()

def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(session)


@router.get("/", response_model=List[UserRead])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all()


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get(user_id)


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create(user_data)


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, update_data: UserUpdate, service: UserService = Depends(get_user_service)):
    return service.update(user_id, update_data)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    service.delete(user_id)
