from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
#from database import get_db
from . import controllers,schemas,services

#router = APIRouter(prefix="/admin", tags=["Administración"])
admin_router = APIRouter(prefix="/admin", tags=["Administración"])

@admin_router.get("/categorias")
def listar_categorias(db: Session = Depends(get_db)):
    return services.listar_categorias(db)


#router = APIRouter(prefix="/datos_negocio", tags=["Datos Negocio"])
# Router para datos_negocio
negocio_router = APIRouter(prefix="/datos_negocio", tags=["Datos Negocio"])

@negocio_router.get("/", response_model=List[schemas.DatosNegocioOut])
def listar_negocios(db: Session = Depends(get_db)):
    return services.get_all_negocios(db)

@negocio_router.get("/{negocio_id}", response_model=schemas.DatosNegocioOut)
def obtener_negocio(negocio_id: int, db: Session = Depends(get_db)):
    negocio = services.get_negocio_by_id(db, negocio_id)
    if not negocio:
        raise HTTPException(status_code=404, detail="Negocio no encontrado")
    return negocio

@negocio_router.post("/", response_model=schemas.DatosNegocioOut)
def crear_negocio(negocio: schemas.DatosNegocioCreate, db: Session = Depends(get_db)):
    return services.create_negocio(db, negocio)

@negocio_router.put("/{negocio_id}", response_model=schemas.DatosNegocioOut)
def actualizar_negocio(negocio_id: int, negocio: schemas.DatosNegocioUpdate, db: Session = Depends(get_db)):
    negocio_actualizado = services.update_negocio(db, negocio_id, negocio)
    if not negocio_actualizado:
        raise HTTPException(status_code=404, detail="Negocio no encontrado")
    return negocio_actualizado

@negocio_router.delete("/{negocio_id}")
def eliminar_negocio(negocio_id: int, db: Session = Depends(get_db)):
    negocio = services.delete_negocio(db, negocio_id)
    if not negocio:
        raise HTTPException(status_code=404, detail="Negocio no encontrado")
    return {"message": "Negocio eliminado correctamente"}


#información de automoviles-
@negocio_router.post("/autos/", response_model=schemas.AutoRead)
def crear_auto_endpoint(auto: schemas.AutoCreate, db: Session = Depends(get_db)):
    return services.crear_auto(db, auto)

@negocio_router.get("/autos/", response_model=list[schemas.AutoRead])
def listar_autos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.obtener_autos(db, skip=skip, limit=limit)

@negocio_router.post("/autos/{id_auto}/detalles/", response_model=schemas.AutoDetalleRead)
def agregar_detalle_auto(id_auto: int, detalle: schemas.AutoDetalleCreate, db: Session = Depends(get_db)):
    return services.crear_detalle_auto(db, id_auto, detalle)
