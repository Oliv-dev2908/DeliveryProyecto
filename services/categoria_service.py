from sqlalchemy.orm import Session
from models.categoria_model import Categoria

def get_categorias(db: Session):
    return db.query(Categoria).all()

def get_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def create_categoria(db: Session, data):
    nueva = Categoria(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def update_categoria(db: Session, categoria_id: int, data):
    categoria = get_categoria(db, categoria_id)
    if not categoria:
        return None
    
    for key, value in data.dict().items():
        setattr(categoria, key, value)
    
    db.commit()
    return categoria

def delete_categoria(db: Session, categoria_id: int):
    categoria = get_categoria(db, categoria_id)
    if not categoria:
        return None
    
    db.delete(categoria)
    db.commit()
    return categoria

def delete_categoria_logic(db: Session, categoria_id: int):
    categoria = get_categoria(db, categoria_id)
    if not categoria:
        return None

    categoria.activo = 0
    db.commit()
    return categoria