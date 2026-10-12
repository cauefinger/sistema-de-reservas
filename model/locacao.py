from database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, Enum
from model.enums import Status

class Locacao(Base):

    __tablename__ = "locacoes"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    recurso_id = Column(Integer, ForeignKey("recursos.id"),nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    data_final = Column(DateTime, nullable=False)
    valor_total = Column(Numeric(10,2), nullable=False)
    status = Column(Enum(Status), nullable=False)
    


