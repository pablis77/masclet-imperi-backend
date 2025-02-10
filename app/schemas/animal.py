from fastapi import FastAPI
from typing import Optional, List
from datetime import date
from pydantic import BaseModel, validator
from enum import Enum

class Genere(str, Enum):
    MASCLE = "M"
    FEMELLA = "F"

class Estado(str, Enum):
    ACTIVO = "activo"
    FALLECIDO = "fallecido"

class AnimalBase:
    def __init__(
        self,
        nom: str,
        explotacio: Optional[str] = None,
        genere: Optional[Genere] = None,
        pare: Optional[str] = None,
        mare: Optional[str] = None,
        quadra: Optional[str] = None,
        cod: Optional[str] = None,
        num_serie: Optional[str] = None,
        dob: Optional[date] = None,
        estado: Optional[Estado] = None,
        part: Optional[date] = None,
        genereT: Optional[Genere] = None,
        estadoT: Optional[Estado] = None,
        alletar: Optional[str] = None
    ):
        self.nom = nom
        self.explotacio = explotacio
        self.genere = genere
        self.pare = pare
        self.mare = mare
        self.quadra = quadra
        self.cod = cod
        self.num_serie = num_serie
        self.dob = dob
        self.estado = estado
        self.part = part
        self.genereT = genereT
        self.estadoT = estadoT
        self.alletar = alletar

class PartoCreate(BaseModel):
    fecha: date
    genere_cria: Genere
    estado_cria: Estado = Estado.ACTIVO

class PartoResponse(PartoCreate):
    id: int
    numero_parto: int

class AnimalCreate(BaseModel):
    nom: str
    explotacio: Optional[str] = None
    genere: Genere
    pare: Optional[str] = None
    mare: Optional[str] = None
    quadra: Optional[str] = None
    cod: Optional[str] = None
    num_serie: Optional[str] = None
    dob: Optional[date] = None
    estado: Estado = Estado.ACTIVO
    alletar: Optional[bool] = None

    @validator('alletar')
    def validate_gender_specific_fields(cls, v, values):
        if 'genere' in values:
            if values['genere'] == Genere.MASCLE:
                if v is not None:
                    raise ValueError('Los machos no pueden tener valores en alletar')
            else:
                if v is None:
                    return False
        return v

class AnimalResponse(AnimalCreate):
    id: int
    partos: List[PartoResponse] = []