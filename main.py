from fastapi import FastAPI
from controller.autenticacao import autenticacao
from database.database import engine, Base
from model.user import Usuario


app = FastAPI()

app.include_router(autenticacao) 

Base.metadata.create_all(bind=engine)

'''
uvicorn main:app --reload
http://127.0.0.1:8000

'''

