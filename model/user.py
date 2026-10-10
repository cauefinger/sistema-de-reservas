from sqlalchemy import Column, String, Boolean, Integer
from database.database import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  
    senha = Column(String, nullable=False)
    ativo = Column(Boolean, nullable=True)
    admin = Column(Boolean, default=False)