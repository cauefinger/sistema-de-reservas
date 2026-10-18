from decimal import Decimal
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.enums import Status
from model.locacao import Locacao
from model.recurso import Recurso
from model.user import Usuario
from schemas.locacao import LocacaoCreateSchemas

def listar_locacao(db: Session):
    return db.query(Locacao).all()

def adicionar_locacao(db: Session, dados: LocacaoCreateSchemas):
    usuario = db.get(Usuario, dados.usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    recurso = db.get(Recurso, dados.recurso_id)
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso não encontrado")
    if not recurso.ativo:
        raise HTTPException(status_code=400, detail="Recurso inativo")
    if recurso.valor_hora is None:
        raise HTTPException(status_code=400, detail="Recurso sem valor por hora definido")

    if dados.data_final <= dados.data_inicio:
        raise HTTPException(status_code=400, detail="data_final deve ser maior que data_inicio")

    conflito = db.query(Locacao).filter(
        Locacao.recurso_id == dados.recurso_id,
        Locacao.status != Status.CANCELADA,
        Locacao.data_inicio < dados.data_final,
        Locacao.data_final > dados.data_inicio,
    ).first()
    if conflito:
        raise HTTPException(status_code=409, detail="Recurso já locado nesse período")

    horas = Decimal(str((dados.data_final - dados.data_inicio).total_seconds())) / Decimal(3600)
    valor_total = (recurso.valor_hora * horas).quantize(Decimal("0.01"))

    novo = Locacao(
        **dados.model_dump(),
        valor_total=valor_total,
        status=Status.PENDENTE,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
