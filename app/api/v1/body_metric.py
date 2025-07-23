from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session, get_user
from ...models.user import User
from ...schemas.body_metrics import (
    BodyMetricsCreate,
    BodyMetricsCreateForm,
    BodyMetricsRead,
    BodyMetricsUpdate,
)
from ...services.body_metrics import BodyMetricsService

router = APIRouter()


def get_service(session: Session = Depends(get_session)) -> BodyMetricsService:
    return BodyMetricsService(session)


@router.get("/", response_model=List[BodyMetricsRead])
def get_all(service: BodyMetricsService = Depends(get_service)):
    return service.get_all()


@router.get("/{metric_id}", response_model=BodyMetricsRead)
def get(metric_id: int, service: BodyMetricsService = Depends(get_service)):
    return service.get(metric_id)


@router.post("/", response_model=BodyMetricsRead, status_code=status.HTTP_201_CREATED)
def create(
    data: BodyMetricsCreateForm,
    service: BodyMetricsService = Depends(get_service),
    user: User = Depends(get_user),
):
    dto = BodyMetricsCreate(user_id=user.id, **data.model_dump())
    return service.create(dto)


@router.put("/{metric_id}", response_model=BodyMetricsRead)
def update(
    metric_id: int,
    update_data: BodyMetricsUpdate,
    service: BodyMetricsService = Depends(get_service),
):
    return service.update(metric_id, update_data)


@router.delete("/{metric_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(metric_id: int, service: BodyMetricsService = Depends(get_service)):
    service.delete(metric_id)


@router.get("/bmi/{metric_id}")
def get_bmi(metric_id: int, service: BodyMetricsService = Depends(get_service)):
    return service.get_bmi(metric_id)


@router.get("/bodyfat/{metric_id}")
def get_bodyfat(metric_id: int, service: BodyMetricsService = Depends(get_service)):
    return service.get_bodyfat(metric_id)
