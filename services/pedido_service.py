from sqlalchemy.orm import Session
from models.pedido_model import Pedido
from datetime import datetime


def crear_pedido(db: Session, data):

    pedido = Pedido(
        cliente_id=data.cliente_id,
        estado="pendiente",
        direccion_entrega=data.direccion_entrega,
        latitud_entrega=data.latitud_entrega,
        longitud_entrega=data.longitud_entrega,
        referencia=data.referencia,
        total=data.total,
        notas=data.notas,
        created_at=datetime.now(),
        updated_at=datetime.now() 
    )

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return pedido


def obtener_pedidos_cliente(db: Session, cliente_id: int):

    return db.query(Pedido).filter(
        Pedido.cliente_id == cliente_id
    ).order_by(Pedido.created_at.desc()).all()


def obtener_pedido(db: Session, pedido_id: int):

    return db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

def obtener_pedidos_repartidor(db: Session, repartidor_id: int):

    return db.query(Pedido).filter(
        Pedido.repartidor_id == repartidor_id
    ).order_by(Pedido.created_at.desc()).all()


def actualizar_estado_pedido(db: Session, pedido_id: int, estado: str):

    pedido = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        return None

    pedido.estado = estado
    pedido.updated_at = datetime.now()

    db.commit()
    db.refresh(pedido)

    return pedido