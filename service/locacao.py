from sqlalchemy.orm import Session
from model.locacao import Locacao
from schemas.locacao import LocacaoCreateSchemas

def listar_locacao(db: Session):
    return db.query(Locacao).all()

def adicionar_locacao(db: Session, dados: LocacaoCreateSchemas):
    novo = Locacao(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

