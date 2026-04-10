from sqlalchemy import Column, Integer, String, Text, Numeric, SmallInteger, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    codigo_qr = Column(String(100))
    precio_unitario = Column(Numeric(10,2), default=0.00)
    unidad_medida = Column(String(30), default="unidad")
    stock_actual = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=5)
    imagen_url = Column(String(255))
    activo = Column(SmallInteger, default=1)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())