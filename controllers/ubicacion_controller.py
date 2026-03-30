from services.ubicacion_service import (
    actualizar_ubicacion,
    obtener_ubicacion_pedido
)


def actualizar_ubicacion_controller(db, body):

    actualizar_ubicacion(db, body)

    return {
        "success": True,
        "data": None
    }


def ubicacion_repartidor_controller(db, pedido_id):

    ubicacion = obtener_ubicacion_pedido(db, pedido_id)

    return {
        "success": True,
        "data": ubicacion
    }