from sqlalchemy.orm import Session
from services.producto_service import obtener_productos


def get_productos(db: Session, categoria_id=None):

    productos = obtener_productos(db, categoria_id)

    return {
        "success": True,
        "data": productos
    }