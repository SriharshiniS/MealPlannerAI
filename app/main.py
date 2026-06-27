from fastapi import FastAPI

from app.core.config import settings
from app.core.database import engine
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.on_event("startup")
def startup():
    connection = engine.connect()
    connection.close()

    logger.info("Database connected successfully")
    logger.info("MealPlannerAI started successfully")


@app.get("/")
def root():
    logger.info("Home endpoint accessed")

    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }