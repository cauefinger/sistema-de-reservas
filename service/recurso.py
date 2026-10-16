from sqlalchemy.orm import Session
from model.recurso import Recurso

def listar_recursos(db: Session):
    return db.query(Recurso).all()
