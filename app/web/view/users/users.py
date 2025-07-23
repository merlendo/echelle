from fastapi import APIRouter, Depends, Request
from sqlmodel import Session

from ....core.dependencies import get_session
from ....core.template import templates
from ....services.user import UserService

router = APIRouter()


def get_user_service(session: Session = Depends(get_session)):
    yield UserService(session)


@router.get("/")
def users_page(request: Request, service: UserService = Depends(get_user_service)):
    # service = UserService(session)
    users = service.get_all()
    return templates.TemplateResponse(
        "users/users.html", {"request": request, "users": users}
    )
