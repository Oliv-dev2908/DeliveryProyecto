from sqlalchemy.orm import Session
from models.producto_model import Producto


def obtener_productos(db: Session, categoria_id=None):

    query = db.query(Producto).filter(Producto.activo == 1)

    if categoria_id:
        query = query.filter(Producto.categoria_id == categoria_id)

    return query.all()