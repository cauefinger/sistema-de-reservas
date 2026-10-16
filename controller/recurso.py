from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from depends import get_db
from schemas.recurso import RecursoGet
from service.recurso import listar_recursos

recurso = APIRouter(
    prefix="/recurso",
    tags=["Recurso"]
)

@recurso.get("/", response_model=List[RecursoGet])
def get_recursos(db: Session = Depends(get_db)):
    return listar_recursos(db)
