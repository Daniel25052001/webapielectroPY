from pydantic import BaseModel

class SedeModel(BaseModel):
    IdSede: int
    Nombre: str
    Direccion: str
    IdCiudad: int
