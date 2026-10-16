from sqlalchemy.orm import Session
from model.locacao import Locacao


def listar_locacao(db: Session):
    return db.query(Locacao).all()