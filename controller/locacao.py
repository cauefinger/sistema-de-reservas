from fastapi import APIRouter


locacao = APIRouter (
    prefix="/",
    tags=["Locação"]
)   

@locacao.get("/")
async def mensagem_rota():
    return{"Mensagem": "Você entrou na rota de locações!"} 
