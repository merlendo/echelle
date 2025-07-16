from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session
from ...schemas.food_log import FoodLogCreate, FoodLogRead, FoodLogUpdate
from ...services.food_log import FoodLogService

router = APIRouter()


def get_service(session: Session = Depends(get_session)) -> FoodLogService:
    return FoodLogService(session)


@router.get("/", response_model=List[FoodLogRead])
def get_all(service: FoodLogService = Depends(get_service)):
    return service.get_all()


@router.get("/{log_id}", response_model=FoodLogRead)
def get(log_id: int, service: FoodLogService = Depends(get_service)):
    return service.get(log_id)


@router.post("/", response_model=FoodLogRead, status_code=status.HTTP_201_CREATED)
def create(data: FoodLogCreate, service: FoodLogService = Depends(get_service)):
    return service.create(data)


@router.put("/{log_id}", response_model=FoodLogRead)
def update(log_id: int, update_data: FoodLogUpdate, service: FoodLogService = Depends(get_service)):
    return service.update(log_id, update_data)


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(log_id: int, service: FoodLogService = Depends(get_service)):
    service.delete(log_id)
