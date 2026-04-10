from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.detalle_pedido_schema import DetallePedidoCreate
from controllers.detalle_pedido_controller import (
    agregar_producto_controller,
    obtener_detalles_controller,
    eliminar_detalle_controller,
    actualizar_cantidad_controller
)

router = APIRouter(prefix="/detalle-pedidos", tags=["Detalle Pedido"])

@router.post("/")
def agregar(body: DetallePedidoCreate, db: Session = Depends(get_db)):
    return agregar_producto_controller(db, body)

@router.get("/pedido/{pedidoId}")
def listar(pedidoId: int, db: Session = Depends(get_db)):
    return obtener_detalles_controller(db, pedidoId)

@router.delete("/{detalleId}")
def eliminar(detalleId: int, db: Session = Depends(get_db)):
    return eliminar_detalle_controller(db, detalleId)

@router.patch("/{detalleId}/cantidad")
def actualizar(detalleId: int, cantidad: int, db: Session = Depends(get_db)):
    return actualizar_cantidad_controller(db, detalleId, cantidad)