from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario,Gasto,Categoria,MetodoPago
from app.api.routes.rutas import rutas

from starlette.responses import RedirectResponse

app=FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)