import os
from datetime import timedelta, timezone, datetime
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 60
EXPIRACAO_DIAS = 7


def gerar_token(dados: dict) -> str:
    payload = dados.copy()
    payload["exp"] = datetime.now (timezone.utc) + timedelta(minutes=EXPIRACAO_MINUTOS) 
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def gerar_refresh_token(dados: dict) -> str:
    payload = dados.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(days=EXPIRACAO_DIAS)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
