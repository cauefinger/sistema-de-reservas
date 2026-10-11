from database.database import Base 
from sqlalchemy import Boolean, String, Integer, Column, Numeric
from model.enums import enum

class Recurso(Base):

    __tablename__ = "Recurso"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(enum, nullable=False)
    valor_hora = Column(Numeric(10,2))
    ativo = Column(Boolean, nullable=False)