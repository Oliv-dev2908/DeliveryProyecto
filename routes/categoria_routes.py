from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.categoria_controller import get_categorias

router = APIRouter()

@router.get("/categorias")
def categorias(db: Session = Depends(get_db)):
    return get_categorias(db)