from pydantic import BaseModel, ConfigDict
from model.enums import TipoRecurso
from decimal import Decimal


class RecursoGet(BaseModel):

    id: int
    nome: str
    tipo: TipoRecurso
    valor_hora: Decimal | None
    ativo: bool

    model_config = ConfigDict(from_attributes=True)


class RecursoCreateSchema(BaseModel):

    nome: str
    tipo: TipoRecurso
    valor_hora: Decimal | None = None
    ativo: bool = True
