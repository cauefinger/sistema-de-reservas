from fastapi import APIRouter, Depends
from typing import List 
from schemas.locacao import LocacaoCreateSchemas, LocacaoGetSchemas
from depends import get_db
from sqlalchemy.orm import Session  
from service.locacao import listar_locacao, adicionar_locacao

locacao = APIRouter (
    prefix="/locacao",
    tags=["Locação"]
)   

@locacao.get("/", response_model=List[LocacaoGetSchemas])
def get_locacao(db: Session = Depends(get_db)):
    return listar_locacao(db)



@locacao.post("/", response_model=LocacaoGetSchemas, status_code=201)
def post_locacao(dados: LocacaoCreateSchemas , db:Session = Depends(get_db)):
    return adicionar_locacao(db, dados)