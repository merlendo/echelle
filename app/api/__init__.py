from fastapi import APIRouter

from .v1 import body_metric, exercice_log, food_log, meal_prep, photo_log, users

router = APIRouter()
router.include_router(body_metric.router, prefix="/body-metrics", tags=["Body Metrics"])
router.include_router(
    exercice_log.router, prefix="/exercise-logs", tags=["Exercise Logs"]
)
router.include_router(food_log.router, prefix="/food-logs", tags=["Food Logs"])
router.include_router(meal_prep.router, prefix="/meal-preps", tags=["Meal Preps"])
router.include_router(photo_log.router, prefix="/photo-logs", tags=["Photo Logs"])
router.include_router(users.router, prefix="/users", tags=["Users"])
