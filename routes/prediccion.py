
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.prediccion import predecir_ventas_producto
from config.database import get_db

router = APIRouter(prefix="/prediccion", tags=["Prediccion"])

@router.get("/{id}/prediccion")
def obtener_prediccion_ventas(id: int, meses: int = 3, db: Session = Depends(get_db)):
    resultado = predecir_ventas_producto(db, id, meses_a_predecir=meses)
    
    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])
        
    return resultado