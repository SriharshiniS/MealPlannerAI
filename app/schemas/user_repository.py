from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, user: UserCreate):

        db_user = User(
            full_name=user.full_name,
            email=user.email,
            hashed_password=user.password   # We'll hash it next lesson
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user