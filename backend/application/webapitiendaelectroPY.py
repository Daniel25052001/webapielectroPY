
#weAPITIENDAELECTRO

from fastapi import FastAPI
from domain.geografia.pais.paismodel import PaisModel
from domain.geografia.departamento.departamentomodel import DepartamentoModel
from domain.geografia.ciudad.ciudadmodel import CiudadModel
app: FastAPI = FastAPI(

    title="Tienda Electro",
    description="API REST de una tienda de electrodomésticos",

)

###########################################

#geografia.pais
@app.get(
    "/paisget",
    summary="Metodo Pais Get",
    description ="Operacion Pais Get",
    tags=["geografia.pais"]
)
async def paisget(idpais: int):
    return idpais

@app.post(
        "/paispost",
        response_model=PaisModel,
        summary="Metodo Pais Post",
        description="Operacion Pais Post",
        tags=["geografia.pais"]
)
async def paispost(pais: PaisModel):
    return pais


@app.put(
        "/paisput",
        response_model=PaisModel,
        summary="Metodo Pais Put",
        description="Operacion Pais Put",
        tags=["geografia.pais"]
)
async def paisput(idciudad: int, ciudadmodel: CiudadModel):
    return ciudadmodel


@app.delete(
        "/paisdelete",
        summary="Metodo Pais Delete",
        description="Operacion Pais Delete",
        tags=["geografia.pais"]
)
async def paisdelete(idpais: int):
    return idpais





#geografia.departamento
@app.get(
    "/departamentoget",
    summary="Metodo Departamento Get",
    description ="Operacion Departamento Get",
    tags=["geografia.departamento"]
)
async def departamentoget(iddepartamento: int):
    return iddepartamento


@app.post(
        "/departamentopost",
        response_model=DepartamentoModel,
        summary="Metodo Departamento Post",
        description="Operacion Departamento Post",
        tags=["geografia.departamento"]
)
async def departamentopost(departamento: DepartamentoModel):
    return departamento


@app.put(
        "/departamentoput",
        response_model=DepartamentoModel,
        summary="Metodo Departamento Put",
        description="Operacion Departamento Put",
        tags=["geografia.departamento"]
)
async def departamentoput(iddepartamento: int, departamentomodel: DepartamentoModel):
    return departamentomodel


@app.delete(
        "/departamentodelete",  
        summary="Metodo Departamento Delete",
        description="Operacion Departamento Delete",
        tags=["geografia.departamento"]
)
async def departamentodelete(iddepartamento: int):
    return iddepartamento






#geografia.ciudad
@app.get(
    "/ciudadget",
    summary="Metodo Ciudad Get",
    description ="Operacion Ciudad Get",
    tags=["geografia.ciudad"]
)
async def ciudadget(idciudad: int):
    return idciudad



@app.post(
        "/ciudadpost",
        response_model=CiudadModel,
        summary="Metodo Ciudad Post",
        description="Operacion Ciudad Post",
        tags=["geografia.ciudad"]
)
async def ciudadpost(ciudad: CiudadModel):
    return ciudad


@app.put(
        "/ciudadput",
        response_model=CiudadModel,
        summary="Metodo Ciudad Put",
        description="Operacion Ciudad Put",
        tags=["geografia.ciudad"]
)
async def ciudadput(idciudad: int, ciudadmodel: CiudadModel):
    return ciudadmodel

@app.delete(
        "/ciudaddelete",
        summary="Metodo Ciudad Delete",
        description="Operacion Ciudad Delete",
        tags=["geografia.ciudad"]
)
async def ciudaddelete(idciudad: int):
    return idciudad

###########################################

###########################################

###########################################

###########################################

###########################################

###########################################

###########################################

###########################################

