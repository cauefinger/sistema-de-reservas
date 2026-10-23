from model.user import Usuario
from schemas.usuario import UsuarioPostSchemas, LoginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from pwdlib import PasswordHash
from security import gerar_token

password_hash = PasswordHash.recommended()


def cadastrar (db: Session, dados: UsuarioPostSchemas):

    novo_usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if novo_usuario:
        raise HTTPException(status_code=409, detail="Usuário com um email já cadastrado.")

    novo_usuario = Usuario( ** dados.model_dump())
    novo_usuario.senha = password_hash.hash(dados.senha)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


def logar(db: Session, dados: LoginSchema):

    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if not usuario or not password_hash.verify(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Senha ou usuário inválidos")

    token = gerar_token({"sub": str(usuario.id)}) # "sub" é do JWT, pega o sujeito em questão da str usuario.id
    return {
        "access_token": token,
        "token_type": "bearer"
}