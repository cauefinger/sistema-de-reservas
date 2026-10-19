from sqlalchemy.orm import Session
from model.locacao import Locacao
from schemas.locacao import LocacaoCreateSchemas
from fastapi import HTTPException
from model.recurso import Recurso


def listar_locacao(db: Session):
    return db.query(Locacao).all()



def adicionar_locacao(db: Session, dados: LocacaoCreateSchemas):

    if dados.data_inicio >= dados.data_final:
        raise HTTPException(status_code=400, detail="Data de início maior ou igual à data final. Tente outra data.")

    recurso = db.get(Recurso, dados.recurso_id)

    if not recurso:
        HTTPException(status_code=404, detail="Recurso não encontrado.")

    if not recurso.ativo:
        HTTPException(status_code=400, detail="Recurso inativo.")

    if recurso.valor_hora is None:
        HTTPException(status_code=400, detail="Recurso sem o valor por hora defenido.")

    novo = Locacao(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

    