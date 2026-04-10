from sqlalchemy.orm import Session
from models.detalle_pedido_model import DetallePedido
from models.producto_model import Producto

def agregar_producto(db: Session, data):

    producto = db.query(Producto).filter(
        Producto.id == data.producto_id,
        Producto.activo == 1
    ).first()

    if not producto:
        return {"error": "Producto no existe"}

    precio = float(producto.precio_unitario)
    subtotal = precio * data.cantidad

    detalle = DetallePedido(
        pedido_id=data.pedido_id,
        producto_id=data.producto_id,
        cantidad=data.cantidad,
        precio_unitario=precio,
        subtotal=subtotal
    )

    db.add(detalle)
    db.commit()
    db.refresh(detalle)

    return detalle

def obtener_detalles(db: Session, pedido_id: int):
    return db.query(DetallePedido).filter(
        DetallePedido.pedido_id == pedido_id
    ).all()

def eliminar_detalle(db: Session, detalle_id: int):

    detalle = db.query(DetallePedido).filter(
        DetallePedido.id == detalle_id
    ).first()

    if not detalle:
        return None

    db.delete(detalle)
    db.commit()

    return {"mensaje": "Eliminado"}

def actualizar_cantidad(db: Session, detalle_id: int, cantidad: int):

    detalle = db.query(DetallePedido).filter(
        DetallePedido.id == detalle_id
    ).first()

    if not detalle:
        return None

    detalle.cantidad = cantidad
    detalle.subtotal = float(detalle.precio_unitario) * cantidad

    db.commit()
    db.refresh(detalle)

    return detalle