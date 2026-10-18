from fastapi import FastAPI
from controller.autenticacao import autenticacao
from controller.locacao import locacao
from controller.recurso import recurso
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
 

 