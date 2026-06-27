from fastapi import FastAPI

from app.core.config import settings
from app.core.database import engine
from app.core.db import Base
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized")
    logger.info("MealPlannerAI started successfully")


@app.get("/")
def root():
    logger.info("Home endpoint accessed")

    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }