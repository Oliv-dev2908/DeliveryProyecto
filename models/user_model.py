from sqlalchemy import Column, Integer, String, SmallInteger
from config.database import Base


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)
    password_hash = Column(String)
    rol = Column(String)
    activo = Column(SmallInteger)