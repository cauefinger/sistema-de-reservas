from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioResponseSchemas, UsuarioPostSchemas
from depends import get_db
from service.usuario import cadastrar

autenticacao = APIRouter(
    prefix="/autenticacao",
    tags=["Autenticação"]
)

@autenticacao.get("/")
async def mensagem_rota():
    return {"mensagem": "Você entrou na rota de autenticação"}


@autenticacao.post("/", response_model=UsuarioResponseSchemas, status_code=201)
def cadastrar_usuario(dados: UsuarioPostSchemas, db: Session = Depends(get_db)):
    return cadastrar(db, dados)
