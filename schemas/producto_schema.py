from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    categoria_id: int
    nombre: str
    descripcion: Optional[str] = None
    codigo_qr: Optional[str] = None
    precio_unitario: float
    unidad_medida: Optional[str] = "unidad"
    stock_actual: Optional[int] = 0
    stock_minimo: Optional[int] = 5
    imagen_url: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int
    activo: int

    class Config:
        from_attributes = True