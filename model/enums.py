from sqlalchemy import Enum
import enum


class Recurso(str, Enum):

    QUADRA = "QUADRA"
    SALA = "SALA"
    ESCRITORIO = "ESCRITORIO"
    SALAO = "SALAO"
    AUDITORIO = "AUDITORIO"
    CAMPO = "CAMPO"
    CHURRASQUEIRA = "CHURRASQUEIRA"
    CONSULTORIO = "CONSULTORIO" 
    ESTUDIO = "ESTUDIO" 
    SALA_DE_AULA =  "SALA_DE_AULA"
    