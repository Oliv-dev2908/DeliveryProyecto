from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_model import User 
from schemas.auth_schema import LoginRequest, TokenFCMRequest
from controllers.auth_controller import login
from services.auth_service import get_current_user 

router = APIRouter(prefix="/api/auth", tags=["Autenticación"])

@router.post("/login")
def login_route(data: LoginRequest, db: Session = Depends(get_db)):
    return login(data, db)

@router.post("/fcm-token")
async def save_fcm_token(
    request: TokenFCMRequest, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == current_user.id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado"
        )
    user.fcm_token = request.fcm_token
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al guardar el token en la base de datos"
        )
    return {
        "success": True, 
        "message": "Dispositivo vinculado correctamente para notificaciones"
    }