from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from . import api, web
from .core.database import engine
from .models import body_metrics, exercise_log, food_log, meal_prep, photo_log, user


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
app = FastAPI(title="Echelle", lifespan=lifespan)

app.include_router(api.router, prefix="/api/v1")
app.include_router(web.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
