from fastapi import APIRouter

recurso = APIRouter(
    prefix="/recurso",
    tags=["Recurso"]
)

@recurso.get("/")
async def mensagem():
    return {"mensagem":"Você entrou na rota de recursos!"}