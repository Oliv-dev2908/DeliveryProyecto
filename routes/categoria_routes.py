from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
import services.categoria_service as service
import schemas.categoria_schema as schema

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/", response_model=list[schema.CategoriaResponse])
def listar(db: Session = Depends(get_db)):
    return service.get_categorias(db)

@router.get("/{id}", response_model=schema.CategoriaResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    return service.get_categoria(db, id)

@router.post("/", response_model=schema.CategoriaResponse)
def crear(data: schema.CategoriaCreate, db: Session = Depends(get_db)):
    return service.create_categoria(db, data)

@router.put("/{id}", response_model=schema.CategoriaResponse)
def actualizar(id: int, data: schema.CategoriaCreate, db: Session = Depends(get_db)):
    return service.update_categoria(db, id, data)

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return service.delete_categoria(db, id)

@router.delete("logic/{id}")
def eliminar_logic(id: int, db: Session = Depends(get_db)):
    return service.delete_categoria_logic(db, id)