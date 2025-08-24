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