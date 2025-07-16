from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session
from ...schemas.meal_prep import MealPrepCreate, MealPrepRead, MealPrepUpdate
from ...services.meal_prep import MealPrepService

router = APIRouter()


def get_service(session: Session = Depends(get_session)) -> MealPrepService:
    return MealPrepService(session)


@router.get("/", response_model=List[MealPrepRead])
def get_all(service: MealPrepService = Depends(get_service)):
    return service.get_all()


@router.get("/{prep_id}", response_model=MealPrepRead)
def get(prep_id: int, service: MealPrepService = Depends(get_service)):
    return service.get(prep_id)


@router.post("/", response_model=MealPrepRead, status_code=status.HTTP_201_CREATED)
def create(data: MealPrepCreate, service: MealPrepService = Depends(get_service)):
    return service.create(data)


@router.put("/{prep_id}", response_model=MealPrepRead)
def update(prep_id: int, update_data: MealPrepUpdate, service: MealPrepService = Depends(get_service)):
    return service.update(prep_id, update_data)


@router.delete("/{prep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(prep_id: int, service: MealPrepService = Depends(get_service)):
    service.delete(prep_id)
