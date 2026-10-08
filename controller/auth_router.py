from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/autenticacao",
    tags="Autenticação"
)

@auth_router.get("/")
async def mensagem_rota():
    return {"mensagem":"Você entrou na rota de autenticação"}