from fastapi import FastAPI
from controller.autenticacao_controller import autenticacao
from controller.locacao_controller import locacao
from controller.recurso_controller import recurso
from database.database import engine, Base
from model.locacao import Locacao
from model.user import Usuario
from model.recurso import Recurso

app = FastAPI()

app.include_router(autenticacao) 
app.include_router(recurso)
app.include_router (locacao)

Base.metadata.create_all(bind=engine)

'''
uvicorn main:app --reload
http://127.0.0.1:8000

'''