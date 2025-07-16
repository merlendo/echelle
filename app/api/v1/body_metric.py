from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session
from ...schemas.body_metrics import (
    BodyMetricsCreate,
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
def create(data: BodyMetricsCreate, service: BodyMetricsService = Depends(get_service)):
    return service.create(data)


@router.put("/{metric_id}", response_model=BodyMetricsRead)
def update(metric_id: int, update_data: BodyMetricsUpdate, service: BodyMetricsService = Depends(get_service)):
    return service.update(metric_id, update_data)


@router.delete("/{metric_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(metric_id: int, service: BodyMetricsService = Depends(get_service)):
    service.delete(metric_id)
