from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Numeric, String, Boolean, TIMESTAMP,DateTime, Text, func
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship
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
    vision = Column(Text)  # Nuevo campo
    mision = Column(Text)  # Nuevo campo
    valores = Column(Text)  # Nuevo campo
    visible = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion = Column(String(100))
    usuario_modificacion = Column(String(100))


class Auto(Base):
    __tablename__ = "autos"
    id_auto = Column(BigInteger, primary_key=True, index=True)
    id_marca_vehiculo = Column(BigInteger, ForeignKey("marcas_vehiculos.id_marca_vehiculo"), nullable=False)
    id_modelo_vehiculo = Column(BigInteger, ForeignKey("modelos_vehiculos.id_modelo_vehiculo"), nullable=False)
    
    marca = relationship("MarcaVehiculo", back_populates="autos")
    modelo = relationship("ModeloVehiculo", back_populates="autos")
    
    anio = Column(Integer, nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(12,2), nullable=False)
    moneda = Column(String(10), default="MXN")
    imagen = Column(Text, nullable=True)
    status = Column(String(50), nullable=True)
    categoria = Column(String(50), nullable=True)
    detalles = Column(Text, nullable=True)
    visible = Column(Boolean, default=True)
    fecha_creacion = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    fecha_modificacion = Column(TIMESTAMP, nullable=True)
    usuario_creacion = Column(String(50), nullable=True)
    usuario_modificacion = Column(String(50), nullable=True)

    detalles_rel = relationship("AutoDetalle", back_populates="auto", cascade="all, delete-orphan")

class MarcaVehiculo(Base):
    __tablename__ = "marcas_vehiculos"
    id_marca_vehiculo = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    autos = relationship("Auto", back_populates="marca")

class ModeloVehiculo(Base):
    __tablename__ = "modelos_vehiculos"
    id_modelo_vehiculo = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    autos = relationship("Auto", back_populates="modelo")


class AutoDetalle(Base):
    __tablename__ = "autos_detalles"

    id_detalle = Column(BigInteger, primary_key=True, index=True)
    id_auto = Column(BigInteger, ForeignKey("autos.id_auto", ondelete="CASCADE"), nullable=False)
    nombre_detalle = Column(String(100), nullable=False)  # Ej: Kilometraje
    valor_detalle = Column(Text, nullable=False)          # Ej: 500 km
    fecha_creacion = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    usuario_creacion = Column(String(50), nullable=True)

    # Relación hacia Auto
    auto = relationship("Auto", back_populates="detalles_rel")