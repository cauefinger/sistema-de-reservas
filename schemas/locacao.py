from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from model.enums import Status
from datetime import datetime

class LocacaoGetSchemas(BaseModel):

    id: int
    usuario_id: int
    recurso_id: int
    data_inicio: datetime
    data_final: datetime
    valor_total: Decimal
    status: Status

    model_config = ConfigDict(from_attributes=True)


class LocacaoCreateSchemas(BaseModel):

    usuario_id: int
    recurso_id: int
    data_inicio: datetime
    data_final: datetime
    valor_total: Decimal
    status: Status

    model_config = ConfigDict(from_attributes=True)