from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    visible: bool = True

class CategoriaResponse(CategoriaBase):
    id_categoria: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True

class DatosNegocioBase(BaseModel):
    nombre_negocio: str
    propietario: Optional[str] = None
    telefono: Optional[str] = None
    correo_electronico: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = None
    codigo_postal: Optional[str] = None
    sitio_web: Optional[str] = None
    redes_sociales: Optional[str] = None
    descripcion: Optional[str] = None
    vision: Optional[str] = None  # Nuevo campo
    mision: Optional[str] = None  # Nuevo campo
    valores: Optional[str] = None  # Nuevo campo
    visible: Optional[bool] = True
    usuario_creacion: Optional[str] = None
    usuario_modificacion: Optional[str] = None

class DatosNegocioCreate(DatosNegocioBase):
    pass

class DatosNegocioUpdate(DatosNegocioBase):
    pass

class DatosNegocioOut(DatosNegocioBase):
    id_negocio: int
    fecha_creacion: Optional[datetime]
    fecha_modificacion: Optional[datetime]

    class Config:
        orm_mode = True

#creacion de automoviles....
#detalles de auto

# Detalles de auto
class AutoDetalleBase(BaseModel):
    nombre_detalle: str
    valor_detalle: str

class AutoDetalleCreate(AutoDetalleBase):
    pass

class AutoDetalleRead(AutoDetalleBase):
    id_detalle: int

    class Config:
        orm_mode = True

class MarcaVehiculoSchema(BaseModel):
    id_marca_vehiculo: int
    nombre: str

    class Config:
        orm_mode = True

class ModeloVehiculoSchema(BaseModel):
    id_modelo_vehiculo: int
    nombre: str

    class Config:
        orm_mode = True


class AutoBase(BaseModel):
    id_marca_vehiculo: int
    id_modelo_vehiculo: int
    anio: int
    descripcion: Optional[str]
    precio: float
    moneda: Optional[str] = "MXN"
    imagen: Optional[str]
    status: Optional[str]
    categoria: Optional[str]
    detalles: Optional[str]

class AutoCreate(AutoBase):
    detalles_rel: Optional[list[AutoDetalleCreate]] = []
    pass  # usado para crear

class AutoRead(BaseModel):
    id_auto: int
    anio: int
    descripcion: Optional[str]
    precio: float
    moneda: Optional[str] = "MXN"
    imagen: Optional[str]
    status: Optional[str]
    categoria: Optional[str]
    detalles: Optional[str]
    marca: MarcaVehiculoSchema
    modelo: ModeloVehiculoSchema
    detalles_rel: list[AutoDetalleRead] = []

    class Config:
        orm_mode = True


