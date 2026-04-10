from sqlalchemy import Column, Integer, String, Text, SmallInteger, TIMESTAMP, func
from config.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    icono_url = Column(String(255))
    activo = Column(SmallInteger, default=1)
    created_at = Column(TIMESTAMP, server_default=func.now())