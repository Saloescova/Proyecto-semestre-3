from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre:str
    edad:int
    telefono:str
    correo:str
    contraseña:str
    fechaRegistro:date
    ciudad:str
    class Config:
        orm_mode=True


class UsuarioDTORespuesta(BaseModel):
    id:int
    nombre:str
    telefono:str
    ciudad:str
    class Config:
        orm_mode=True

class GastoDTOPeticion(BaseModel):
    monto:float
    fecha:date
    descipcion:str
    nombre:str
    class Config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    id:int
    monto:float
    fecha:date
    descripcion:str
    class Config:
        orm_mode=True

class CategoriaDTOPeticion(BaseModel):
    nombreCategoria:str
    descripcion:str
    fotoicono:str
orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    id:int
    nombreCategoria:str
    descripcion:str
    fotoicono:str
orm_mode=True

class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo:str
    descripcion:str
    class Config:
        orm_mode=True

class MetodoPagoDTORespuesta(BaseModel):
    id:int
    nombreMetodo:str
    descripcion:str
    class Config:
        orm_mode=True

class FacturaDTOPeticion(BaseModel):
    pass

class FacturaDTORespuesta(BaseModel):
    pass