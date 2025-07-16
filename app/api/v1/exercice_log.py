from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session
from ...schemas.exercise_log import (
    ExerciseLogCreate,
    ExerciseLogRead,
    ExerciseLogUpdate,
)
from ...services.exercise_log import ExerciseLogService

router = APIRouter()


def get_service(session: Session = Depends(get_session)) -> ExerciseLogService:
    return ExerciseLogService(session)


@router.get("/", response_model=List[ExerciseLogRead])
def get_all(service: ExerciseLogService = Depends(get_service)):
    return service.get_all()


@router.get("/{log_id}", response_model=ExerciseLogRead)
def get(log_id: int, service: ExerciseLogService = Depends(get_service)):
    return service.get(log_id)


@router.post("/", response_model=ExerciseLogRead, status_code=status.HTTP_201_CREATED)
def create(data: ExerciseLogCreate, service: ExerciseLogService = Depends(get_service)):
    return service.create(data)


@router.put("/{log_id}", response_model=ExerciseLogRead)
def update(log_id: int, update_data: ExerciseLogUpdate, service: ExerciseLogService = Depends(get_service)):
    return service.update(log_id, update_data)


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(log_id: int, service: ExerciseLogService = Depends(get_service)):
    service.delete(log_id)
