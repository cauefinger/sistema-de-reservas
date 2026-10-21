from fastapi import APIRouter, Depends
from typing import List 
from schemas.locacao import LocacaoCreateSchemas, LocacaoGetSchemas
from depends import get_db
from sqlalchemy.orm import Session  
from service.locacao import listar_locacao, adicionar_locacao


#TODO: renomear esse arquivo para para seguir o padrão de sufixo *_controller.py

locacao = APIRouter (
    prefix="/locacao",
    tags=["Locação"]
)   

#TODO: deve se chamar find_all para seguir a convencao de nomes de API REST
@locacao.get("/", response_model=List[LocacaoGetSchemas])
def get_locacao(db: Session = Depends(get_db)):
    return listar_locacao(db)


#TODO: deve se chamar create para seguir a convencao de nomes de API REST
@locacao.post("/", response_model=LocacaoGetSchemas, status_code=201)
def post_locacao(dados: LocacaoCreateSchemas , db:Session = Depends(get_db)):
    return adicionar_locacao(db, dados)