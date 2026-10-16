from fastapi import APIRouter, Depends
from typing import List 
from schemas.locacao import LocacaoGet
from depends import get_db
from sqlalchemy.orm import Session  
from service.locacao import listar_locacao

locacao = APIRouter (
    prefix="/locacao",
    tags=["Locação"]
)   

@locacao.get("/", response_model=List[LocacaoGet])
def get_locacao(db: Session = Depends(get_db)):
    return listar_locacao(db)