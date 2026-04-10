from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_model import User 
from schemas.auth_schema import LoginRequest, TokenFCMRequest
from controllers.auth_controller import login

router = APIRouter(prefix="/api/auth", tags=["Autenticación"])

@router.post("/login")
def login_route(data: LoginRequest, db: Session = Depends(get_db)):
    return login(data, db)

@router.post("/fcm-token")
async def save_fcm_token(
    request: TokenFCMRequest, 
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == request.user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user.fcm_token = request.fcm_token
    db.commit()
    
    return {"success": True, "message": "Token vinculado al usuario " + str(request.user_id)}
