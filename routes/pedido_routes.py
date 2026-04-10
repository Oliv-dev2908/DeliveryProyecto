from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.pedido_schema import CrearPedidoRequest, ActualizarEstadoRequest
from services.notification_service import NotificationService
from models.user_model import User
from controllers.pedido_controller import (
    crear_pedido_controller,
    pedidos_cliente_controller,
    pedido_detalle_controller,
    pedidos_repartidor_controller,
    actualizar_estado_controller,
    pedidos_sin_repartidor_controller,
    asignar_repartidor_controller,
    pedidos_controller
    )
from schemas.pedido_schema import AsignarRepartidorRequest

router = APIRouter()

@router.post("/pedidos")
def crear_pedido(request: CrearPedidoRequest, db: Session = Depends(get_db)):
    return crear_pedido_controller(db, request)

@router.get("/pedidos")
def pedidos_controller(db: Session = Depends(get_db)):
    return pedidos_controller(db)

@router.get("/pedidos/cliente/{clienteId}")
def pedidos_cliente(clienteId: int, db: Session = Depends(get_db)):
    return pedidos_cliente_controller(db, clienteId)

@router.get("/pedidos/sin-repartidor")
def pedidos_sin_repartidor(db: Session = Depends(get_db)):
    return pedidos_sin_repartidor_controller(db)

@router.get("/pedidos/{pedidoId}")
def pedido_detalle(pedidoId: int, db: Session = Depends(get_db)):
    return pedido_detalle_controller(db, pedidoId)

@router.get("/pedidos/repartidor/{repartidorId}")
def pedidos_repartidor(repartidorId: int, db: Session = Depends(get_db)):
    return pedidos_repartidor_controller(db, repartidorId)

@router.patch("/pedidos/{pedidoId}/estado")
def actualizar_estado(
    pedidoId: int,
    body: ActualizarEstadoRequest,
    db: Session = Depends(get_db)
):
    return actualizar_estado_controller(db, pedidoId, body)


@router.patch("/pedidos/{pedidoId}/asignar-repartidor")
def asignar_repartidor(
    pedidoId: int,
    body: AsignarRepartidorRequest,
    db: Session = Depends(get_db)
):
    return asignar_repartidor_controller(db, pedidoId, body)