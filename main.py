from typing import Union
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Datos(BaseModel):
    porcentaje_agua: str
    estado_bomba: bool

datos = {}

@app.get("/")
def read_root():
    return "Servidor de Acualink"

@app.get("/api/datos")
async def obtener_datos():
    return {
        "porcentaje_agua": datos.get("porcentaje_agua", "No hay datos"),
        "estado_bomba": datos.get("estado_bomba", "No hay datos")
    }
    
@app.post("/api/datos")
async def recibir_datos(data: Datos):
    datos["porcentaje_agua"] = data.porcentaje_agua
    datos["estado_bomba"] = data.estado_bomba
    return {"status": "Datos recibidos", "Datos": datos}