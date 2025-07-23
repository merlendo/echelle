from fastapi import APIRouter, Depends, Form, Request
from sqlmodel import Session

from ....core.dependencies import get_session, get_user
from ....core.template import templates
from ....models.user import User
from ....services.body_metrics import BodyMetricsService

router = APIRouter()


@router.get("/weight")
def weight_page(
    request: Request,
    user: User = Depends(get_user),
):
    return templates.TemplateResponse(
        "body_metrics/weigth.html",
        {"request": request},
    )


@router.post("/weight")
def weight_post(
    request: Request,
    session: Session = Depends(get_session),
):
    service = BodyMetricsService(session)
    users = service.get_all()
    return templates.TemplateResponse(
        "users/users.html", {"request": request, "users": users}
    )
