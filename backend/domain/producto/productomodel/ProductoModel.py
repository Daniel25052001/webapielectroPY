
from pydantic import BaseModel

class ProductoModel(BaseModel):
    IdProducto: int
    Nombre: str
    Descripcion: str
    Precio: float
    Stock: int
    IdCategoria: int
    IdMarca: int
    IdModelo: int
