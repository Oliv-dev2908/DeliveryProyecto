from sqlalchemy.orm import Session
from schemas.auth_schema import LoginRequest
from services.auth_service import login_user
from fastapi import HTTPException


def login(data: LoginRequest, db: Session):

    user = login_user(db, data.email, data.password)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    return {
        "success": True,
        "token": "token_ejemplo",
        "usuario": {
            "id": user.id,
            "nombre": user.nombre,
            "apellido": user.apellido,
            "email": user.email,
            "rol": user.rol
        }
    }