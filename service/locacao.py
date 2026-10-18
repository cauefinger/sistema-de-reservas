from sqlalchemy.orm import Session
from model.locacao import Locacao
from schemas.locacao import LocacaoCreateSchemas
from fastapi import HTTPException

def listar_locacao(db: Session):
    return db.query(Locacao).all()



def adicionar_locacao(db: Session, dados: LocacaoCreateSchemas):

    if dados.data_inicio >= dados.data_final:
        raise HTTPException(status_code=400, detail="Data de início maior ou igual à data final. Tente outra data.")
    
    novo = Locacao(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

    