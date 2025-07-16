from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from ...core.dependencies import get_session
from ...schemas.photo_log import PhotoLogCreate, PhotoLogRead, PhotoLogUpdate
from ...services.photo_log import PhotoLogService

router = APIRouter()


def get_service(session: Session = Depends(get_session)) -> PhotoLogService:
    return PhotoLogService(session)


@router.get("/", response_model=List[PhotoLogRead])
def get_all(service: PhotoLogService = Depends(get_service)):
    return service.get_all()


@router.get("/{photo_id}", response_model=PhotoLogRead)
def get(photo_id: int, service: PhotoLogService = Depends(get_service)):
    return service.get(photo_id)


@router.post("/", response_model=PhotoLogRead, status_code=status.HTTP_201_CREATED)
def create(data: PhotoLogCreate, service: PhotoLogService = Depends(get_service)):
    return service.create(data)


@router.put("/{photo_id}", response_model=PhotoLogRead)
def update(photo_id: int, update_data: PhotoLogUpdate, service: PhotoLogService = Depends(get_service)):
    return service.update(photo_id, update_data)


@router.delete("/{photo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(photo_id: int, service: PhotoLogService = Depends(get_service)):
    service.delete(photo_id)
