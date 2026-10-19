from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioPostSchemas
from depends import get_db

autenticacao = APIRouter(
    prefix="/autenticacao",
    tags=["Autenticação"]
)

@autenticacao.get("/")
async def mensagem_rota():
    return {"mensagem": "Você entrou na rota de autenticação"}


@autenticacao.post("/", response_model=UsuarioPostSchemas, status_code=201)
def cadastrar_usuario(dados: UsuarioPostSchemas, db: Session = Depends(get_db)):
    return
