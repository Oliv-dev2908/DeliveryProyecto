from sqlalchemy.orm import Session
from services.categoria_service import obtener_categorias


def get_categorias(db: Session):

    categorias = obtener_categorias(db)

    return {
        "success": True,
        "data": categorias
    }