from typing import Optional, List, Dict, Any
from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class Genere(str, Enum):
    """Enumeración de géneros posibles"""
    MASCLE = "M"
    FEMELLA = "F"

class Estat(str, Enum):
    """Enumeración de estados posibles"""
    ACTIU = "ACTIU"
    MORT = "MORT"
    VENUT = "VENUT"
    TRASLLAT = "TRASLLAT"

class PartoStats(BaseModel):
    total: int
    vius: int
    morts: int
    venuts: int
    ultima_data: Optional[date]
    
    model_config = ConfigDict(from_attributes=True)

class PartoBase(BaseModel):
    fecha: date = Field(..., description="Data del part")
    genere_cria: Genere
    estat_cria: Estat = Field(default=Estat.ACTIU, description="Estat actual de la cria")
    observacions: Optional[str] = Field(None, max_length=500)
    
    model_config = ConfigDict(from_attributes=True)

class PartoCreate(PartoBase):
    pass

class PartoResponse(PartoBase):
    id: int
    numero_parto: int

class AnimalBase(BaseModel):
    alletar: bool = False
    explotacio: str
    nom: str
    genere: str
    pare: Optional[str] = None
    mare: Optional[str] = None
    quadra: str
    cod: str
    num_serie: str
    dob: Optional[date] = None
    estado: str
    part: int = 0
    genere_t: Optional[str] = None
    estado_t: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class AnimalCreate(AnimalBase):
    pass

class AnimalUpdate(AnimalBase):
    alletar: Optional[bool] = None
    explotacio: Optional[str] = None
    nom: Optional[str] = None
    genere: Optional[str] = None
    quadra: Optional[str] = None
    cod: Optional[str] = None
    num_serie: Optional[str] = None
    estado: Optional[str] = None
    part: Optional[int] = None

class AnimalListItem(BaseModel):
    """Modelo para listado de animales"""
    nom: str
    cod: Optional[str] = None
    dob: Optional[date] = None
    genere: Genere
    estat: Estat  # Changed from estado to estat for consistency
    alletar: bool
    num_partos: int = 0
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "nom": "Blanquita",
                "cod": "B123",
                "genere": "F",
                "estat": "ACTIU",
                "alletar": True,
                "num_partos": 2
            }
        }
    )

class AnimalResponse(AnimalBase):
    id: int
    created_at: date
    updated_at: date

class AnimalDetail(AnimalResponse):
    pass

class AnimalDetail(BaseModel):
    general: Dict[str, Any] = Field(..., description="Dades generals")
    partos: List[Dict[str, Any]] = Field(default_factory=list, description="Historial de parts")
    stats: PartoStats = Field(..., description="Estadístiques dels parts")
    
    model_config = ConfigDict(from_attributes=True)

class ExplotacioStats(BaseModel):
    """Modelo para estadísticas de explotación"""
    total: int = Field(..., description="Total d'animals")
    machos: int = Field(..., description="Total mascles")
    hembras: int = Field(..., description="Total femelles")
    terneros: int = Field(..., description="Total alletant")
    fecha: datetime = Field(..., description="Data actualització")
    
    model_config = ConfigDict(from_attributes=True)

class ExplotacioResponse(BaseModel):
    explotacio: str
    total: int

    model_config = ConfigDict(from_attributes=True)