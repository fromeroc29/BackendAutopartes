from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP,DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import datetime
#from app.config.database import Base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    visible = Column(Boolean, default=True)
    fecha_creacion = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class DatosNegocio(Base):
    __tablename__ = "datos_negocio"

    id_negocio = Column(Integer, primary_key=True, index=True)
    nombre_negocio = Column(String(255), nullable=False)
    propietario = Column(String(255))
    telefono = Column(String(50))
    correo_electronico = Column(String(255))
    direccion = Column(String(255))
    ciudad = Column(String(100))
    estado = Column(String(100))
    pais = Column(String(100))
    codigo_postal = Column(String(20))
    sitio_web = Column(String(255))
    redes_sociales = Column(String(255))
    descripcion = Column(String(500))
    visible = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String(100))
    usuario_modificacion = Column(String(100))