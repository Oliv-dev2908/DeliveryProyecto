from sqlalchemy import Column, Integer, ForeignKey, Numeric
from config.database import Base

class DetallePedido(Base):
    __tablename__ = "detalle_pedidos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10,2), nullable=False)
    subtotal = Column(Numeric(10,2), nullable=False)