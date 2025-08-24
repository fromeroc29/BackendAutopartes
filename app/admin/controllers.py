from sqlalchemy.orm import Session
from . import services

def listar_categorias(db: Session):
    return services.get_categorias(db)
