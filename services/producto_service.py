from sqlalchemy.orm import Session
from models.producto_model import Producto

def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, data):
    nuevo = Producto(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_producto(db: Session, producto_id: int, data):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    for key, value in data.dict().items():
        setattr(producto, key, value)

    db.commit()
    return producto

def delete_producto(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    db.delete(producto)
    db.commit()
    return producto

def delete_producto_logic(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    producto.activo = 0
    db.commit()
    return producto