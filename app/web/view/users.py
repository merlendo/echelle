from fastapi import APIRouter, Depends, Request
from sqlmodel import Session

from ...core.dependencies import get_session
from ...core.template import templates
from ...services.user import UserService

router = APIRouter()

@router.get("/")
def users_page(request: Request, session: Session = Depends(get_session)):
    service = UserService(session)
    users = service.get_users()
    return templates.TemplateResponse("users/users.html", {"request": request, "users": users})
