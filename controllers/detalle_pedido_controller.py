from services.detalle_pedido_service import (
    agregar_producto,
    obtener_detalles,
    eliminar_detalle,
    actualizar_cantidad
)

def agregar_producto_controller(db, body):
    return agregar_producto(db, body)

def obtener_detalles_controller(db, pedido_id):
    return obtener_detalles(db, pedido_id)

def eliminar_detalle_controller(db, detalle_id):
    return eliminar_detalle(db, detalle_id)

def actualizar_cantidad_controller(db, detalle_id, cantidad):
    return actualizar_cantidad(db, detalle_id, cantidad)