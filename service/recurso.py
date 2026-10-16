from sqlalchemy.orm import Session
from model.recurso import Recurso
from schemas.recurso import RecursoCreateSchema

def listar_recursos(db: Session):
    return db.query(Recurso).all()


def cadastrar_recurso(db: Session, dados: RecursoCreateSchema):
    novo = Recurso(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo