from fastapi import APIRouter

autenticacao = APIRouter(
    prefix="/autenticacao",
    tags=["Autenticação"]
)

@autenticacao.get("/")
async def mensagem_rota():
    return {"mensagem": "Você entrou na rota de autenticação"}