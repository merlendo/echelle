from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..core.template import templates
from .view.users import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users")

@router.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})