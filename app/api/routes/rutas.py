from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Dependes
from app.api.schemas.DTO import UsuarioDTOPeticion,UsuarioDTORespuesta
from app.api.models.modelosApp import Usuario
from app.database.configuration import sessionLocal,engine
from app.api.models.modelosApp import Gasto
from app.api.schemas.DTO import GastoDTOPeticion,GastoDTORespuesta
from app.api.models.modelosApp import Categoria
from app.api.schemas.DTO import CategoriaDTOPeticion,CategoriaDTORespuesta
from app.api.models.modelosApp import MetodoPago
from app.api.schemas.DTO import MetodoPagoDTOPeticion,MetodoPagoDTORespuesta

#Para que un api funciones debe tener un archivo enrutador
rutas=APIRouter() #Endpoint

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()
    
#PROGRAMACIÓN DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Dependes(getDataBase)):
    try:
        usuario=Usuario(
        nombre=datosPeticion.nombre,
        edad=datosPeticion.edad,
        telefono=datosPeticion.telefono,
        correo=datosPeticion.correo, 
        contraseña=datosPeticion.contraseña,
        fechaRegistro=datosPeticion.fechaRegistro,
        ciudad=datosPeticion.ciudad

        )
        db.add(usuario) #agrego
        db.commit()     #ejecuto
        db.refresh(usuario)  #refresco
        return usuario
    
    except Exception as error:
         db.rollback()
         raise HTTPException(status_code=400,detail="Error al registrar usuario") #Para levantar la Exception

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Dependes(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return listadoDeUsuarios
    except Exception as error:
        db.rollback()#frena la operacion
        raise HTTPException(status_code=400,detail="Error al registrar el usuario")

@rutas.put("/usuarios")
def cambiarUsuarios():
    pass

@rutas.delete("/usuarios")
def eliminarUsuarios():
    pass

#Rutas Gastos

@rutas.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion:GastoDTOPeticion, db:Session=Dependes(getDataBase)):
    try:  
        gasto=Gasto(
        monto=datosPeticion.monto,
        fecha=datosPeticion.fecha,
        descipcion=datosPeticion.descipcion,
        nombre=datosPeticion.nombre

        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return gasto

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail="Error al registrar el gasto")

@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGastos(db:Session=Dependes(getDataBase)):
    try:
        listadoDeGastos=db.query(Usuario).all()
        return listadoDeGastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail="Error al registrat el usuario")

@rutas.put("/gastos")
def cambiarGasto():
    pass

@rutas.delete("/gastos")
def eliminarGasto():
    pass
    
@rutas.post("/categorias", response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion:CategoriaDTOPeticion, db:Session=Dependes(getDataBase)):
    try:
        categoria=Categoria(
        nombreCategoria=datosPeticion.nombreCategoria,
        descripcion=datosPeticion.descripcion,
        fotoicono=datosPeticion.fotoicono
        
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail="Error al registrar la categoria")
    
@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db:Session=Dependes(getDataBase)):
    try:
        listadoDeCategoria=db.query(Usuario).all()
        return listadoDeCategoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail="Error al registrat el usuario")

@rutas.put("/categoria")
def cambiarCategoria():
    pass

@rutas.delete("/categoria")
def eliminarCategoria():
    pass

@rutas.post("/metodos_pagos", response_model=MetodoPagoDTORespuesta)
def guardarCategoria(datosPeticion:MetodoPagoDTOPeticion, db:Session=Dependes(getDataBase)):
    try:
        metodo_pago=MetodoPago(
        nombreMetodo=datosPeticion.nombreMetodo,
        descripcion=datosPeticion.descripcion
        
        )

        db.add(metodo_pago)
        db.commit()
        db.refresh(metodo_pago)
        return metodo_pago
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail="Error al registrar el metodo de pago")
    
@rutas.get("/metodopago", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago(db:Session=Dependes(getDataBase)):
    try:
        listadoDeMetodoPago=db.query(Usuario).all()
        return listadoDeMetodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail="Error al registrat el usuario")

@rutas.put("/metodo_pago")
def cambiarMetodoPago():
    pass

@rutas.delete("/metodo_pago")
def eliminarMetodoPago():
    pass