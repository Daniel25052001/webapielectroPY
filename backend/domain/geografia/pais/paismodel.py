
#PaisModel

from pydantic import BaseModel

class PaisModel(BaseModel):
    IdPais: int
    Nombre: str