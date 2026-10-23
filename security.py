import os
from datetime import timedelta, timezone, datetime
import jwt

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 60


def gerar_token(dados: dict) -> str:
    payload = dados.copy()
    payload["exp"] = datetime.now (timezone.utc) + timedelta(minutes=EXPIRACAO_MINUTOS) 
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)