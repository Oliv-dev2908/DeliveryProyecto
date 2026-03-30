from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime
from config.database import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer)
    repartidor_id = Column(Integer)

    estado = Column(String)

    direccion_entrega = Column(String)
    latitud_entrega = Column(Numeric)
    longitud_entrega = Column(Numeric)

    referencia = Column(String)

    total = Column(Numeric)

    notas = Column(Text)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)