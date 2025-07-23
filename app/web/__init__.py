from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..core.template import templates
from .view.body_metrics import weight
from .view.users import users

router = APIRouter()
router.include_router(users.router, prefix="/users")
router.include_router(weight.router, prefix="/body_metrics")


@router.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
