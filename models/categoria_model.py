from sqlalchemy import Column, Integer, String, Text, SmallInteger, DateTime
from config.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)

    nombre = Column(String)
    descripcion = Column(Text)
    icono_url = Column(String)

    activo = Column(SmallInteger)

    created_at = Column(DateTime)