def optimizar_ruta(data):

    origen = data.get("origen")
    destino = data.get("destino")

    return {
        "distancia": 2.5,
        "tiempo_estimado": 8,
        "ruta": [
            origen,
            destino
        ]
    }