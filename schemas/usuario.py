from pydantic import BaseModel, ConfigDict


class UsuarioPostSchemas(BaseModel):

    nome: str
    email: str
    senha: str
    ativo: str
    admin: bool

    model_config = ConfigDict(from_attributes=True)