from app.auth.security import verify_password
from app.auth.jwt import create_access_token
from app.schemas.user import UserLogin

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.security import hash_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):

    hashed_password = hash_password(user.password)

    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def authenticate_user(db: Session, user: UserLogin):

    db_user = get_user_by_email(db, user.email)

    if not db_user:
        return None

    if not verify_password(user.password, db_user.hashed_password):
        return None

    token = create_access_token(
    {
        "sub": db_user.email,
    }
)
    return {
        "access_token": token,
        "token_type": "bearer",
    }