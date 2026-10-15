from fastapi import APIRouter, Depends
from typing import List 
from schemas.locacao import LocacaoGet
from depends import get_db
from sqlalchemy.orm import Session  
from model.locacao import Locacao

locacao = APIRouter (
    prefix="/locacao",
    tags=["Locação"]
)   

@locacao.get("/", response_model=List[LocacaoGet])
async def mensagem_rota(db: Session = Depends(get_db)):
    return db.query(Locacao).all()
