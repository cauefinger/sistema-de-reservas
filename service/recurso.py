from sqlalchemy.orm import Session
from model.recurso import Recurso
from schemas.recurso import RecursoCreateSchema

#TODO: Esse arquivo deve ter o sufixo _service, já que se trata de um service. recurso_service.py

#TODO: seguir o padrão de nomes de CRUD find_by_id, find_all, create, update, delete (perguntar pra IA)

#TODO: service não deve fazer conexão com banco de dados, apenas transformar dados. classes service não devem "conhecer" a classe db.
# As classes que fazem essa busca no banco de dados se chamam repository.

#TODO: aqui deve chamar find_all
def listar_recursos(db: Session):
    return db.query(Recurso).all()

#TODO: aqui deve chamar create
def cadastrar_recurso(db: Session, dados: RecursoCreateSchema):
    novo = Recurso(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo