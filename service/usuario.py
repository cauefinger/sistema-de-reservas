from model.user import Usuario
from schemas.usuario import UsuarioPostSchemas
from sqlalchemy.orm import Session
from controller.autenticacao import UsuarioPostSchemas
from fastapi import HTTPException


def cadastrar (db: Session, dados: UsuarioPostSchemas):

    novo_usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if novo_usuario:
        raise HTTPException(status_code=409, detail="Usuário com um email já cadastrado.")


    novo_usuario = Usuario( ** dados.model_dump())

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario