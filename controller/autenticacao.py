from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioResponseSchemas, UsuarioPostSchemas, LoginSchema
from depends import get_db
from service.usuario import cadastrar, logar

#TODO: renomear esse arquivo para autenticacao_controller.py para seguir o padrão de sufixo *_controller.py

autenticacao = APIRouter(
    prefix="/autenticacao",
    tags=["Autenticação"]
)

@autenticacao.get("/")
async def mensagem_rota():
    return {"mensagem": "Você entrou na rota de autenticação"}


#TODO: deve se chamar create para seguir a convencao de nomes de API REST
@autenticacao.post("/", response_model=UsuarioResponseSchemas, status_code=201)
def cadastrar_usuario(dados: UsuarioPostSchemas, db: Session = Depends(get_db)):
    return cadastrar(db, dados)


#TODO: deve se chamar login para seguir a convencao de nomes de API REST, logar já é pressuposto que é um usuario, adicionar
# usuario no nome do metodo fica redundante.
@autenticacao.post("/login", status_code=200)
def logar_usuario(dados: LoginSchema, db: Session = Depends(get_db)):
    return