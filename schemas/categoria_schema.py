from pydantic import BaseModel

class CategoriaResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    icono_url: str

    class Config:
        from_attributes = True