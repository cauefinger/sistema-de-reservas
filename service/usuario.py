from model.user import Usuario
from schemas.usuario import UsuarioPostSchemas, LoginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

#TODO: Esse arquivo deve ter o sufixo _service, já que se trata de um service
#TODO: seguir o padrão de nomes de CRUD find_by_id, find_all, create, update, delete (perguntar pra IA)
#TODO: service não deve fazer conexão com banco de dados, apenas transformar dados. classes service não devem "conhecer" a classe db.
# As classes que fazem essa busca no banco de dados se chamam repository.

#TODO: aqui deve chamar create
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

    return #retornar token