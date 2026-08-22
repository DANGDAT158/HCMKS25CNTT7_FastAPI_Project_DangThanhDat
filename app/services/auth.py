from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def register_user(db: Session, user_data: UserCreate):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return None
    password_hash = hash_password(
        user_data.password
    )
    user = User(
        email=user_data.email,
        password_hash=password_hash,
        full_name=user_data.full_name
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user