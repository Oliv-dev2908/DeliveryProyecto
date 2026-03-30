from services.ruta_service import optimizar_ruta


def ruta_optimizada_controller(body):

    ruta = optimizar_ruta(body)

    return {
        "success": True,
        "data": ruta
    }