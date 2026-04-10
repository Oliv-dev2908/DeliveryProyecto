from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    icono_url: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int
    activo: int

    class Config:
        from_attributes = True