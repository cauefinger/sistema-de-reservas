from fastapi import APIRouter

recurso = APIRouter(
    prefix="/recurso",
    tags=["Recurso"]
)

@recurso.get("/")
async def mensagem():
    return {"mensagem":"Os recursos disponíveis atualmente são: "}