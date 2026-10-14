from database.database import Base 
from sqlalchemy import Boolean, String, Integer, Column, Numeric, Enum
from model.enums import TipoRecurso

class Recurso(Base):

    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(Enum(TipoRecurso), nullable=False)
    valor_hora = Column(Numeric(10,2))
    ativo = Column(Boolean, nullable=False)