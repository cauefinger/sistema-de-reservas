from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioResponseSchemas, UsuarioPostSchemas, LoginSchema
from depends import get_db
from service.usuario import cadastrar, logar

autenticacao = APIRouter(
    prefix="/autenticacao",
    tags=["Autenticação"]
)

@autenticacao.get("/")
async def mensagem_rota():
    return {"mensagem": "Você entrou na rota de autenticação"}


@autenticacao.post("/create", response_model=UsuarioResponseSchemas, status_code=201)
def cadastrar_usuario(dados: UsuarioPostSchemas, db: Session = Depends(get_db)):
    return cadastrar(db, dados)


@autenticacao.post("/login", status_code=200)
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    return logar(db, dados)