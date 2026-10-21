from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from depends import get_db
from schemas.recurso import RecursoGet, RecursoCreateSchema
from service.recurso import listar_recursos, cadastrar_recurso


#TODO: renomear esse arquivo para para seguir o padrão de sufixo *_controller.py

recurso = APIRouter(
    prefix="/recurso",
    tags=["Recurso"]
)

#TODO: deve se chamar find_all para seguir a convencao de nomes de API REST
@recurso.get("/", response_model=List[RecursoGet])
def get_recursos(db: Session = Depends(get_db)):
    return listar_recursos(db)

#TODO: deve se chamar create para seguir a convencao de nomes de API REST
@recurso.post("/", response_model=RecursoGet, status_code=201)
def post_recursos(dados: RecursoCreateSchema, db: Session = Depends(get_db)):
    return cadastrar_recurso(db, dados)