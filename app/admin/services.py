from sqlalchemy.orm import Session
from . import models,schemas
from app.admin import models

#datos de categorias

def listar_categorias(db: Session):
    categorias = db.query(models.Categoria).filter(models.Categoria.visible == True).all()
    
    # para depurar
    for cat in categorias:
        print("ID:", cat.id_categoria)
    
    return categorias

#datos de negocio

def get_all_negocios(db: Session):
    return db.query(models.DatosNegocio).all()

def get_negocio_by_id(db: Session, negocio_id: int):
    return db.query(models.DatosNegocio).filter(models.DatosNegocio.id_negocio == negocio_id).first()

def create_negocio(db: Session, negocio: schemas.DatosNegocioCreate):
    db_negocio = models.DatosNegocio(**negocio.dict())
    db.add(db_negocio)
    db.commit()
    db.refresh(db_negocio)
    return db_negocio

def update_negocio(db: Session, negocio_id: int, negocio_data: schemas.DatosNegocioUpdate):
    db_negocio = get_negocio_by_id(db, negocio_id)
    if not db_negocio:
        return None
    for key, value in negocio_data.dict(exclude_unset=True).items():
        setattr(db_negocio, key, value)
    db.commit()
    db.refresh(db_negocio)
    return db_negocio

def delete_negocio(db: Session, negocio_id: int):
    db_negocio = get_negocio_by_id(db, negocio_id)
    if not db_negocio:
        return None
    db.delete(db_negocio)
    db.commit()
    return db_negocio