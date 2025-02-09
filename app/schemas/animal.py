from pydantic import BaseModel
from datetime import date
from typing import Optional

class AnimalBase(BaseModel):
    nom: str
    explotacio: Optional[str] = None
    genere: Optional[str] = None
    pare: Optional[str] = None
    mare: Optional[str] = None
    quadra: Optional[str] = None
    cod: Optional[str] = None
    num_serie: Optional[str] = None
    dob: Optional[date] = None
    estado: Optional[str] = None
    part: Optional[date] = None
    genereT: Optional[str] = None
    estadoT: Optional[str] = None
    alletar: Optional[str] = None

class AnimalCreate(AnimalBase):
    pass

class AnimalResponse(AnimalBase):
    id: int

    class Config:
        from_attributes = True