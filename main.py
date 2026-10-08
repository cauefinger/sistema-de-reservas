from fastapi import FastAPI

app = FastAPI()


from controller import auth_router


app.include_router(auth_router)