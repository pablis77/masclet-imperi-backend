from fastapi import FastAPI
from fastapi.param_functions import Body
from typing import Optional
from datetime import date

class AnimalBase:
    def __init__(
        self,
        nom: str,
        explotacio: Optional[str] = None,
        genere: Optional[str] = None,
        pare: Optional[str] = None,
        mare: Optional[str] = None,
        quadra: Optional[str] = None,
        cod: Optional[str] = None,
        num_serie: Optional[str] = None,
        dob: Optional[date] = None,
        estado: Optional[str] = None,
        part: Optional[date] = None,
        genereT: Optional[str] = None,
        estadoT: Optional[str] = None,
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

class AnimalCreate(AnimalBase):
    pass

class AnimalResponse(AnimalBase):
    id: int