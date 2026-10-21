from pydantic import BaseModel, ConfigDict


class UsuarioPostSchemas(BaseModel): # o que a API espera receber do usuário

    nome: str
    email: str
    senha: str
    ativo: bool
    admin: bool

    model_config = ConfigDict(from_attributes=True)


class UsuarioResponseSchemas(BaseModel): # parâmetro que a API deve devolver ao usuário, usando o response model para validar e filtrar.    

    id: int
    nome: str
    email: str
    ativo: bool
    admin: bool

    model_config = ConfigDict(from_attributes=True)

class LoginSchema(BaseModel):

    email: str
    senha: str