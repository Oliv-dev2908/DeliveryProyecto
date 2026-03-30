from sqlalchemy.orm import Session
from models.categoria_model import Categoria


def obtener_categorias(db: Session):

    return db.query(Categoria).filter(
        Categoria.activo == 1
    ).all()