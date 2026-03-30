from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user_model import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_password(password, hash):
    return pwd_context.verify(password, hash)


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email,
        User.activo == 1
    ).first()

    if not user:
        return None

    if not verificar_password(password, user.password_hash):
        return None

    return user