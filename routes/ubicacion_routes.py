from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db

from schemas.ubicacion_schema import UbicacionRepartidor
from controllers.ubicacion_controller import (
    actualizar_ubicacion_controller,
    ubicacion_repartidor_controller
)

router = APIRouter()

@router.post("/ubicacion/actualizar")
def actualizar_ubicacion(
    body: UbicacionRepartidor,
    db: Session = Depends(get_db)
):
    return actualizar_ubicacion_controller(db, body)


@router.get("/ubicacion/repartidor/{pedidoId}")
def ubicacion_repartidor(
    pedidoId: int,
    db: Session = Depends(get_db)
):
    return ubicacion_repartidor_controller(db, pedidoId)