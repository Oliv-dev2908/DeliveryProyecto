from pydantic import BaseModel
from typing import Optional

class ProductoResponse(BaseModel):
    id: int
    categoria_id: int
    nombre: str
    descripcion: Optional[str]
    precio_unitario: float
    unidad_medida: str
    stock_actual: int
    imagen_url: Optional[str]

    class Config:
        from_attributes = True