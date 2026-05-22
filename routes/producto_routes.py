import traceback

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
import services.producto_service as service
import schemas.producto_schema as schema

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=list[schema.ProductoResponse])
def listar(db: Session = Depends(get_db)):
    try:
        # 2. Intentamos hacer la consulta
        productos = service.get_productos(db)
        return productos
    except Exception as e:
        # 3. Imprimimos el error exacto en la consola de Uvicorn
        print("🔥 ERROR EXACTO:")
        traceback.print_exc()
        # 4. Devolvemos el error a la pantalla (Postman/Android/Navegador)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}", response_model=schema.ProductoResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    return service.get_producto(db, id)

@router.post("/", response_model=schema.ProductoResponse)
def crear(data: schema.ProductoCreate, db: Session = Depends(get_db)):
    return service.create_producto(db, data)

@router.put("/{id}", response_model=schema.ProductoResponse)
def actualizar(id: int, data: schema.ProductoCreate, db: Session = Depends(get_db)):
    return service.update_producto(db, id, data)

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return service.delete_producto(db, id)

@router.delete("logic/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return service.delete_producto_logic(db, id)