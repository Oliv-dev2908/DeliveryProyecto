from sqlalchemy.orm import Session
from models.pedido_model import Pedido
from models.producto_model import Producto
from models.detalle_pedido_model import DetallePedido
from schemas.pedido_schema import CrearPedidoRequest
from datetime import datetime


from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

def crear_pedido(db: Session, data: CrearPedidoRequest):
    try:
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

        db.flush() 

        for item in data.detalles:
            producto = db.query(Producto).filter(
                Producto.id == item.producto_id,
                Producto.activo == 1
            ).first()

            if not producto:
                db.rollback() 
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"El producto con ID {item.producto_id} no existe o no está activo."
                )

            precio = float(producto.precio_unitario)
            subtotal = precio * item.cantidad

            detalle = DetallePedido(
                pedido_id=pedido.id,  
                producto_id=item.producto_id,
                cantidad=item.cantidad,
                precio_unitario=precio,
                subtotal=subtotal
            )
            db.add(detalle)

        db.commit()
        db.refresh(pedido)
        return pedido

    except SQLAlchemyError as e:
        db.rollback()
        
        error_orig = str(e.__dict__.get('orig', e))
        
        if "Stock insuficiente" in error_orig:
            import re
            match = re.search(r'EXCEPTION:\s*(.*)', error_orig)
            mensaje_limpio = match.group(1) if match else "Stock insuficiente en uno de los productos."
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=mensaje_limpio)
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error en la base de datos: {error_orig}"
        )


def obtener_pedidos_cliente(db: Session, cliente_id: int):

    return db.query(Pedido).filter(
        Pedido.cliente_id == cliente_id
    ).order_by(Pedido.created_at.desc()).all()

def obtener_pedidos(db: Session):
    return db.query(Pedido).order_by(Pedido.created_at.desc()).all()

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

def obtener_pedidos_sin_repartidor(db: Session):
    return db.query(Pedido).filter(
        Pedido.repartidor_id == None
    ).order_by(Pedido.created_at.desc()).all()


def asignar_repartidor(db: Session, pedido_id: int, repartidor_id: int):

    pedido = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        return None

    pedido.repartidor_id = repartidor_id
    pedido.estado = "asignado"
    pedido.updated_at = datetime.now()

    db.commit()
    db.refresh(pedido)

    return pedido