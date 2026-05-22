from pydantic import BaseModel
from typing import Optional, List

class CrearPedidoRequest(BaseModel):

    cliente_id: int
    direccion_entrega: str
    latitud_entrega: float
    longitud_entrega: float
    referencia: Optional[str]
    total: float
    notas: Optional[str]
    detalles: List[ItemPedidoRequest]

class ItemPedidoRequest(BaseModel):
    producto_id: int
    cantidad: int


class PedidoResponse(BaseModel):

    id: int
    cliente_id: int
    estado: str
    direccion_entrega: str
    total: float

    class Config:
        from_attributes = True

class ActualizarEstadoRequest(BaseModel):
    estado: str

class AsignarRepartidorRequest(BaseModel):
    repartidor_id: int