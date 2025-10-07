

from pydantic import BaseModel

class EmpresaModel(BaseModel):
    nombre: str
    IdEmpresa: int
    Nit: str
    Direccion: str
    