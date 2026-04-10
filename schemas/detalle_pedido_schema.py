from pydantic import BaseModel

class DetallePedidoCreate(BaseModel):
    pedido_id: int
    producto_id: int
    cantidad: int

class DetallePedidoResponse(BaseModel):
    id: int
    pedido_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float

    class Config:
        from_attributes = True