from pydantic import BaseModel
from typing import Optional

class CrearPedidoRequest(BaseModel):

    cliente_id: int
    direccion_entrega: str
    latitud_entrega: float
    longitud_entrega: float
    referencia: Optional[str]
    total: float
    notas: Optional[str]


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