from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.database import engine


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)