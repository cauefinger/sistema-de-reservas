from pydantic import BaseModel, ConfigDict
from sqlalchemy import DateTime, DECIMAL
from model.enums import Status

class LocacaoGet(BaseModel):

    id: int
    usuario_id: int
    recurso_id: int
    data_inicio: DateTime
    data_final: DateTime
    valor_total: DECIMAL
    status: Status

    model_config = ConfigDict(from_attributes=True)