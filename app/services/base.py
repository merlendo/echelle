from typing import Generic, List, Type, TypeVar

from fastapi import HTTPException, status
from sqlmodel import Session, select

T = TypeVar("T")  # Model
C = TypeVar("C")  # Creation schema
U = TypeVar("U")  # Update schema


class BaseService(Generic[T, C, U]):
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def create(self, data: C) -> T:
        obj = self.model.model_validate(data)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get(self, obj_id: int) -> T:
        obj = self.session.get(self.model, obj_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} with ID {obj_id} not found.",
            )
        return obj

    def get_all(self) -> List[T]:
        return self.session.exec(select(self.model)).all()

    def update(self, obj_id: int, update_data: U) -> T:
        obj = self.get(obj_id)
        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(obj, key, value)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, obj_id: int) -> None:
        obj = self.get(obj_id)
        self.session.delete(obj)
        self.session.commit()
