from fastapi import FastAPI

app = FastAPI()


'''
uvicorn main:app --reload
http://127.0.0.1:8000
'''
from controller import auth_router

app.include_router(auth_router)