#CiudadModel
from pydantic import BaseModel

class CiudadModel(BaseModel):
    IdCiudad: int
    Nombre: str
    IdDepartamento: int