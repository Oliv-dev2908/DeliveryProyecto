from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.producto_controller import get_productos

router = APIRouter()

@router.get("/productos")
def productos(categoria_id: int = None, db: Session = Depends(get_db)):
    return get_productos(db, categoria_id)