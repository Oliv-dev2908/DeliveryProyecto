from sqlalchemy.orm import Session
from models.ubicacion_model import UbicacionRepartidor
from datetime import datetime


def actualizar_ubicacion(db: Session, data):

    ubicacion = UbicacionRepartidor(
        pedido_id=data.pedido_id,
        repartidor_id=data.repartidor_id,
        latitud=data.latitud,
        longitud=data.longitud,
        velocidad=data.velocidad,
        timestamp=datetime.now()
    )

    db.add(ubicacion)
    db.commit()

    return True


def obtener_ubicacion_pedido(db: Session, pedido_id: int):

    return db.query(UbicacionRepartidor).filter(
        UbicacionRepartidor.pedido_id == pedido_id
    ).order_by(
        UbicacionRepartidor.timestamp.desc()
    ).first()