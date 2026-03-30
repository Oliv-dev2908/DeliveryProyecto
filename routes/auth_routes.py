from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.auth_controller import login
from schemas.auth_schema import LoginRequest

router = APIRouter()

@router.post("/api/auth/login")
def login_route(data: LoginRequest, db: Session = Depends(get_db)):
    return login(data, db)