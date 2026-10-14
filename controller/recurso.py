from fastapi import APIRouter, Depends
from schemas.recurso import RecursoGet
from sqlalchemy.orm import Session  
from depends import get_db
from model.recurso import Recurso
from typing import List


recurso = APIRouter(
    prefix="/recurso",
    tags=["Recurso"]
)

@recurso.get("/", response_model=List[RecursoGet])
def listar_recursos(db: Session = Depends(get_db)):
    return db.query(Recurso).all()  