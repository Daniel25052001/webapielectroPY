
from pydantic import BaseModel

class DepartamentoModel(BaseModel):
    IdDepartamento: int
    Nombre: str
    IdPais: int