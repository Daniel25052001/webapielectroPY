
#weAPITIENDAELECTRO

from fastapi import FastAPI
from domain.geografia.pais.paismodel import PaisModel
from domain.geografia.departamento.departamentomodel import DepartamentoModel
from domain.geografia.ciudad.ciudadmodel import CiudadModel
from domain.producto.categoria.categoriamodel import CategoriaModel
from domain.producto.marca.marcamodel import MarcaModel
from domain.producto.modelo.modelomodel import ModeloModel
from domain.usuario.genero.generomodel import GeneroModel
from domain.usuario.tipodocumento.tipodocumentomodel import TipoDocumentoModel
from domain.transaccion.estadodeventa.estadoventamodel import EstadoDeVentaModel
from domain.usuario.genero.generomodel import GeneroModel
from domain.usuario.nombre.nombremodel import NombreModel
from domain.usuario.tipodocumento.tipodocumentomodel import TipoDocumentoModel
from domain.organizacion.empleado.empleadomodel import EmpleadoModel
from domain.organizacion.empresa.empresamodel import EmpresaModel
from domain.organizacion.sede.sedemodel import SedeModel



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

# organizacion.empleado
@app.get(
    "/empleadoget",
    summary="Método Empleado Get",
    description="Operación Empleado Get",
    tags=["organizacion.empleado"]
)
async def empleadoget(idempleado: int):
    return idempleado


@app.post(
    "/empleadopost",
    response_model=EmpleadoModel,
    summary="Método Empleado Post",
    description="Operación Empleado Post",
    tags=["organizacion.empleado"]
)
async def empleadopost(empleado: EmpleadoModel):
    return empleado


@app.put(
    "/empleadoput",
    response_model=EmpleadoModel,
    summary="Método Empleado Put",
    description="Operación Empleado Put",
    tags=["organizacion.empleado"]
)
async def empleadoput(idempleado: int, empleadomodel: EmpleadoModel):
    return empleadomodel


@app.delete(
    "/empleadodelete",
    summary="Método Empleado Delete",
    description="Operación Empleado Delete",
    tags=["organizacion.empleado"]
)
async def empleadodelete(idempleado: int):
    return idempleado



#organizacion.empresa
@app.get(
    "/empresaget",
    summary="Método Empresa Get",
    description="Operación Empresa Get",
    tags=["organizacion.empresa"]
)
async def empresaget(idempresa: int):
    return idempresa


@app.post(
    "/empresapost",
    response_model=EmpresaModel,
    summary="Método Empresa Post",
    description="Operación Empresa Post",
    tags=["organizacion.empresa"]
)
async def empresapost(empresa: EmpresaModel):
    return empresa


@app.put(
    "/empresaput",
    response_model=EmpresaModel,
    summary="Método Empresa Put",
    description="Operación Empresa Put",
    tags=["organizacion.empresa"]
)
async def empresaput(idempresa: int, empresamodel: EmpresaModel):
    return empresamodel


@app.delete(
    "/empresadelete",
    summary="Método Empresa Delete",
    description="Operación Empresa Delete",
    tags=["organizacion.empresa"]
)
async def empresadelete(idempresa: int):
    return idempresa


#organizacion.sede
@app.get(
    "/sedget",
    summary="Método Sede Get",
    description="Operación Sede Get",
    tags=["organizacion.sede"]
)
async def sedget(idsede: int):
    return idsede


@app.post(
    "/sedpost",
    response_model=SedeModel,
    summary="Método Sede Post",
    description="Operación Sede Post",
    tags=["organizacion.sede"]
)
async def sedpost(sede: SedeModel):
    return sede


@app.put(
    "/sedput",
    response_model=SedeModel,
    summary="Método Sede Put",
    description="Operación Sede Put",
    tags=["organizacion.sede"]
)
async def sedput(idsede: int, sedemodel: SedeModel):
    return sedemodel


@app.delete(
    "/seddelete",
    summary="Método Sede Delete",
    description="Operación Sede Delete",
    tags=["organizacion.sede"]
)
async def seddelete(idsede: int):
    return idsede

###########################################
#producto.categoria
@app.get(
    "/categoriaget",
    summary="Método Categoria Get",
    description="Operación Categoria Get", 
    tags=["producto.categoria"]
)
async def categoriaget(idcategoria: int):
    return idcategoria  


@app.post(
    "/categoriapost",
    response_model=CategoriaModel,
    summary="Método Categoria Post",
    description="Operación Categoria Post",
    tags=["producto.categoria"]
)
async def categoriapost(categoria: CategoriaModel):
    return categoria


@app.put(
    "/categoriaput",
    response_model=CategoriaModel,
    summary="Método Categoria Put",
    description="Operación Categoria Put",
    tags=["producto.categoria"]
)
async def categoriaput(idcategoria: int, categoriamodel: CategoriaModel):
    return categoriamodel  


@app.delete(
    "/categoriadelete",
    summary="Método Categoria Delete",
    description="Operación Categoria Delete",
    tags=["producto.categoria"]
)
async def categoriadelete(idcategoria: int):
    return idcategoria


#producto.marca
@app.get(
    "/marcaget",
    summary="Método Marca Get",
    description="Operación Marca Get",
    tags=["producto.marca"]
)
async def marcaget(idmarca: int):
    return idmarca


@app.post(
    "/marcapost",
    response_model=MarcaModel,
    summary="Método Marca Post",
    description="Operación Marca Post",
    tags=["producto.marca"]
)
async def marcapost(marca: MarcaModel):
    return marca    

@app.put(
    "/marcaput",    
    response_model=MarcaModel,
    summary="Método Marca Put",
    description="Operación Marca Put",
    tags=["producto.marca"]
)
async def marcaput(idmarca: int, marcamodel: MarcaModel):
    return marcamodel   

@app.delete(
    "/marcadelete", 
    summary="Método Marca Delete",
    description="Operación Marca Delete",
    tags=["producto.marca"]
)
async def marcadelete(idmarca: int):
    return idmarca  



#producto.modelo
@app.get(
    "/modeloget",
    summary="Método Modelo Get",
    description="Operación Modelo Get",
    tags=["producto.modelo"]
)
async def modeloget(idmodelo: int):
    return idmodelo 

@app.post(
    "/modelopost",
    response_model=ModeloModel,
    summary="Método Modelo Post",
    description="Operación Modelo Post",
    tags=["producto.modelo"]
)
async def modelopost(modelo: ModeloModel):
    return modelo   

@app.put(
    "/modeloput",       
    response_model=ModeloModel,
    summary="Método Modelo Put",
    description="Operación Modelo Put",
    tags=["producto.modelo"]
)
async def modeloput(idmodelo: int, modelomodel: ModeloModel):
    return modelomodel  

@app.delete(
    "/modelodelete",        
    summary="Método Modelo Delete",
    description="Operación Modelo Delete",
    tags=["producto.modelo"]
)
async def modelodelete(idmodelo: int):
    return idmodelo     

###########################################
# usuario.genero
@app.get(
    "/generoget",
    summary="Método Género Get",
    description="Operación Género Get",
    tags=["usuario.genero"]
)
async def generoget(idgenero: int):
    return idgenero


@app.post(
    "/generopost",
    response_model=GeneroModel,
    summary="Método Género Post",
    description="Operación Género Post",
    tags=["usuario.genero"]
)
async def generopost(genero: GeneroModel):
    return genero


@app.put(
    "/generoput",
    response_model=GeneroModel,
    summary="Método Género Put",
    description="Operación Género Put",
    tags=["usuario.genero"]
)
async def generoput(idgenero: int, generomodel: GeneroModel):
    return generomodel


@app.delete(
    "/generodelete",
    summary="Método Género Delete",
    description="Operación Género Delete",
    tags=["usuario.genero"]
)
async def generodelete(idgenero: int):
    return idgenero



#usuario.nombre
@app.get(
    "/nombreget",
    summary="Método Nombre Get",
    description="Operación Nombre Get",
    tags=["usuario.nombre"]
)
async def nombreget(idnombre: int):
    return idnombre


@app.post(
    "/nombrepost",
    response_model=NombreModel,
    summary="Método Nombre Post",
    description="Operación Nombre Post",
    tags=["usuario.nombre"]
)
async def nombrepost(nombre: NombreModel):
    return nombre


@app.put(
    "/nombreput",
    response_model=NombreModel,
    summary="Método Nombre Put",
    description="Operación Nombre Put",
    tags=["usuario.nombre"]
)
async def nombreput(idnombre: int, nombremodel: NombreModel):
    return nombremodel


@app.delete(
    "/nombredelete",
    summary="Método Nombre Delete",
    description="Operación Nombre Delete",
    tags=["usuario.nombre"]
)
async def nombredelete(idnombre: int):
    return idnombre

#usuario.tipodocumento

@app.get(
    "/tipodocumentoget",
    summary="Método TipoDocumento Get",
    description="Operación TipoDocumento Get",
    tags=["usuario.tipodocumento"]
)
async def tipodocumentoget(idtipodocumento: int):
    return idtipodocumento


@app.post(
    "/tipodocumentopost",
    response_model=TipoDocumentoModel,
    summary="Método TipoDocumento Post",
    description="Operación TipoDocumento Post",
    tags=["usuario.tipodocumento"]
)
async def tipodocumentopost(tipodocumento: TipoDocumentoModel):
    return tipodocumento


@app.put(
    "/tipodocumentoput",
    response_model=TipoDocumentoModel,
    summary="Método TipoDocumento Put",
    description="Operación TipoDocumento Put",
    tags=["usuario.tipodocumento"]
)
async def tipodocumentoput(idtipodocumento: int, tipodocumentomodel: TipoDocumentoModel):
    return tipodocumentomodel


@app.delete(
    "/tipodocumentodelete",
    summary="Método TipoDocumento Delete",
    description="Operación TipoDocumento Delete",
    tags=["usuario.tipodocumento"]
)
async def tipodocumentodelete(idtipodocumento: int):
    return idtipodocumento


###########################################
# transaccion.estadoventa
@app.get(
    "/estadoventaget",
    summary="Método EstadoVenta Get",
    description="Operación EstadoVenta Get",
    tags=["transaccion.estadoventa"]
)
async def estadoventaget(idestado: int):
    return idestado


@app.post(
    "/estadoventapost",
    response_model=EstadoDeVentaModel,
    summary="Método EstadoVenta Post",
    description="Operación EstadoVenta Post",
    tags=["transaccion.estadoventa"]
)
async def estadoventapost(estadoventa: EstadoDeVentaModel):
    return estadoventa


@app.put(
    "/estadoventaput",
    response_model=EstadoDeVentaModel,
    summary="Método EstadoVenta Put",
    description="Operación EstadoVenta Put",
    tags=["transaccion.estadoventa"]
)
async def estadoventaput(idestado: int, estadoventamodel: EstadoDeVentaModel):
    return estadoventamodel


@app.delete(
    "/estadoventadelete",
    summary="Método EstadoVenta Delete",
    description="Operación EstadoVenta Delete",
    tags=["transaccion.estadoventa"]
)
async def estadoventadelete(idestado: int):
    return idestado









































###########################################

###########################################

###########################################

###########################################

###########################################

###########################################

###########################################

