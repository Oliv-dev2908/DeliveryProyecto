from sqlalchemy.orm import Session
from models.user_model import User
from services.notification_service import NotificationService
from firebase_admin import messaging
from services.pedido_service import (
    crear_pedido,
    obtener_pedidos_cliente,
    obtener_pedido,
    obtener_pedidos_repartidor,
    actualizar_estado_pedido,
    obtener_pedidos_sin_repartidor,
    asignar_repartidor,
    obtener_pedidos
)

def crear_pedido_controller(db: Session, request):
    pedido = crear_pedido(db, request)
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title="🛠️ ¡Nuevo Pedido Disponible!",
                body="Hay un pedido esperando en la ferretería. ¡Aceptalo ahora!"
            ),
            topic="pedidos_disponibles"
        )
        messaging.send(message)
    except Exception as e:
        print(f"Error en notificación de tema: {e}")

    return {
        "success": True,
        "data": pedido
    }

def actualizar_estado_controller(db: Session, pedido_id, body):
    pedido = actualizar_estado_pedido(db, pedido_id, body.estado)

    if not pedido:
        return {"success": False, "message": "Pedido no encontrado"}

    cliente = db.query(User).filter(User.id == pedido.cliente_id).first()
    if cliente and cliente.fcm_token:
        titulos = {
            "confirmado": "Pedido Confirmado",
            "en_camino": "Tu pedido va en camino",
            "entregado": "Pedido Entregado"
        }
        NotificationService.send_push_notification(
            token=cliente.fcm_token,
            title=titulos.get(body.estado, "Actualización de Pedido"),
            body=f"Tu pedido #{pedido_id} ahora está: {body.estado}",
            data={"pedido_id": str(pedido_id)}
        )

    return {
        "success": True,
        "data": pedido
    }

def asignar_repartidor_controller(db: Session, pedido_id, body):
    pedido = asignar_repartidor(db, pedido_id, body.repartidor_id)
    repartidor = db.query(User).filter(User.id == body.repartidor_id).first()
    if repartidor and repartidor.fcm_token:
        NotificationService.send_push_notification(
            token=repartidor.fcm_token,
            title="📦 ¡Nuevo Pedido Asignado!",
            body=f"Se te ha asignado el pedido #{pedido_id}. Revisa los detalles.",
            data={"pedido_id": str(pedido_id)}
        )

    return {
        "success": True,
        "data": pedido
    }


def pedidos_cliente_controller(db: Session, cliente_id):
    pedidos = obtener_pedidos_cliente(db, cliente_id)
    return {"success": True, "data": pedidos}

def pedidos_controller(db: Session):
    pedidos = obtener_pedidos(db)
    return {"success": True, "data": pedidos}

def pedido_detalle_controller(db: Session, pedido_id):
    pedido = obtener_pedido(db, pedido_id)
    return {"success": True, "data": pedido}

def pedidos_repartidor_controller(db: Session, repartidor_id):
    pedidos = obtener_pedidos_repartidor(db, repartidor_id)
    return {"success": True, "data": pedidos}

def pedidos_sin_repartidor_controller(db):
    pedidos = obtener_pedidos_sin_repartidor(db)
    return {
        "success": True,
        "data": pedidos
    }
