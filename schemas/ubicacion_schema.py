from pydantic import BaseModel
from datetime import datetime

class UbicacionRepartidor(BaseModel):

    pedido_id: int
    repartidor_id: int
    latitud: float
    longitud: float
    velocidad: float
    timestamp: datetime