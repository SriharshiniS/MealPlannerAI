import os

from sqlalchemy import create_engine

from app.core.config import settings

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)