from sqlalchemy.orm import Session
from model.locacao import Locacao
from schemas.locacao import LocacaoCreateSchemas
from fastapi import HTTPException
from model.recurso import Recurso
from decimal import Decimal
from model.enums import Status

def listar_locacao(db: Session):
    return db.query(Locacao).all()



def adicionar_locacao(db: Session, dados: LocacaoCreateSchemas):

    if dados.data_inicio >= dados.data_final:
        raise HTTPException(status_code=400, detail="Data de início maior ou igual à data final. Tente outra data.")

    recurso = db.get(Recurso, dados.recurso_id)

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso não encontrado.")

    if not recurso.ativo:
        raise HTTPException(status_code=400, detail="Recurso inativo.")

    if recurso.valor_hora is None:
        raise HTTPException(status_code=400, detail="Recurso sem o valor por hora defenido.")


    horas = (dados.data_final - dados.data_inicio).total_seconds() / 3600

    valor_total = (Decimal(str(horas)) * recurso.valor_hora)


    novo = Locacao(**dados.model_dump(), valor_total=valor_total, status=Status.PENDENTE)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

    