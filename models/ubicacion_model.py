from sqlalchemy import Column, Integer, Float, DateTime, Numeric
from config.database import Base

class UbicacionRepartidor(Base):

    __tablename__ = "ubicaciones_repartidor"

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer)
    repartidor_id = Column(Integer)

    latitud = Column(Numeric)
    longitud = Column(Numeric)

    velocidad = Column(Float)

    timestamp = Column(DateTime)