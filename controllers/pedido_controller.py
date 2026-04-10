from sqlalchemy.orm import Session
from services.pedido_service import (
    crear_pedido,
    obtener_pedidos_cliente,
    obtener_pedido,
    obtener_pedidos_repartidor,
    actualizar_estado_pedido,
    obtener_pedidos_sin_repartidor,
    asignar_repartidor
)


def crear_pedido_controller(db: Session, request):

    pedido = crear_pedido(db, request)

    return {
        "success": True,
        "data": pedido
    }


def pedidos_cliente_controller(db: Session, cliente_id):

    pedidos = obtener_pedidos_cliente(db, cliente_id)

    return {
        "success": True,
        "data": pedidos
    }


def pedido_detalle_controller(db: Session, pedido_id):

    pedido = obtener_pedido(db, pedido_id)

    return {
        "success": True,
        "data": pedido
    }

def pedidos_repartidor_controller(db: Session, repartidor_id):

    pedidos = obtener_pedidos_repartidor(db, repartidor_id)

    return {
        "success": True,
        "data": pedidos
    }

def actualizar_estado_controller(db: Session, pedido_id, body):

    pedido = actualizar_estado_pedido(db, pedido_id, body.estado)

    if not pedido:
        return {
            "success": False,
            "message": "Pedido no encontrado"
        }

    return {
        "success": True,
        "data": pedido
    }


def pedidos_sin_repartidor_controller(db):
    return obtener_pedidos_sin_repartidor(db)

def asignar_repartidor_controller(db, pedido_id, body):
    return asignar_repartidor(db, pedido_id, body.repartidor_id)