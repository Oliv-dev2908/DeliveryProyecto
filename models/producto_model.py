from sqlalchemy import Column, Integer, String, Text, Numeric, SmallInteger, DateTime
from config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    categoria_id = Column(Integer)

    nombre = Column(String)
    descripcion = Column(Text)
    codigo_qr = Column(String)

    precio_unitario = Column(Numeric)
    unidad_medida = Column(String)

    stock_actual = Column(Integer)
    stock_minimo = Column(Integer)

    imagen_url = Column(String)

    activo = Column(SmallInteger)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)