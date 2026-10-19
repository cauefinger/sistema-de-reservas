from pydantic import BaseModel, ConfigDict


class UsuarioPostSchemas(BaseModel):

    nome: str
    email: str
    senha: str
    ativo: bool
    admin: bool

    model_config = ConfigDict(from_attributes=True)


class UsuarioResponseSchemas(BaseModel):

    id: int
    nome: str
    email: str
    ativo: bool
    admin: bool

    model_config = ConfigDict(from_attributes=True)
