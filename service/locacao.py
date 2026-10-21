from sqlalchemy.orm import Session
from model.locacao import Locacao
from schemas.locacao import LocacaoCreateSchemas
from fastapi import HTTPException
from model.recurso import Recurso
from decimal import Decimal
from model.enums import Status

def listar_locacao(db: Session):
    return db.query(Locacao).all()

#TODO: Esse arquivo deve ter o sufixo _service, já que se trata de um service. locacao_service.py, para distinguir do locacao.py (model)

#TODO: ajustar espaçamento, pesquisar por PEP8
#TODO: seguir o padrão de nomes de CRUD find_by_id, find_all, create, update, delete (perguntar pra IA)

#TODO: service não deve fazer conexão com banco de dados, apenas transformar dados. classes service não devem "conhecer" a classe db.
# As classes que fazem essa busca no banco de dados se chamam *_repository.py.

#TODO: aqui deve chamar create
def adicionar_locacao(db: Session, dados: LocacaoCreateSchemas):

    if dados.data_inicio >= dados.data_final:
        raise HTTPException(status_code=400, detail="Data de início maior ou igual à data final. Tente outra data.")

    recurso = db.get(Recurso, dados.recurso_id)



    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso não encontrado.")

    if not recurso.ativo:
        raise HTTPException(status_code=400, detail="Recurso inativo.")

    if recurso.valor_hora is None:
        raise HTTPException(status_code=400, detail="Recurso sem o valor por hora definido.")


    horas = (dados.data_final - dados.data_inicio).total_seconds() / 3600

    valor_total = (Decimal(str(horas)) * recurso.valor_hora)

   
    conflito = db.query(Locacao).filter(
        Locacao.recurso_id == dados.recurso_id,
        Locacao.status != Status.CANCELADA,
        Locacao.data_inicio < dados.data_final,
        Locacao.data_final > dados.data_inicio,
    ).first()

    if conflito:
        raise HTTPException(status_code=409, detail="Já existe uma locação nesse período.")

    novo = Locacao(**dados.model_dump(), valor_total=valor_total, status=Status.PENDENTE)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

    