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
    nom: str = Field(..., min_length=1, max_length=100, description="Nom de l'animal")
    cod: Optional[str] = Field(None, max_length=50, description="Codi identificatiu")
    num_serie: Optional[str] = Field(None, max_length=50, description="Número de serie")
    alletar: bool = Field(default=False, description="Indica si està alletant")
    estat: Estat = Field(default=Estat.ACTIU, description="Estat actual")
    genere: Genere = Field(..., description="Gènere de l'animal")
    explotacio: str = Field(..., description="Codi de l'explotació")
    
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    @field_validator('alletar')
    def validate_alletar(cls, v: bool, values: Dict[str, Any]) -> bool:
        if 'genere' in values.data and values.data['genere'] == Genere.MASCLE and v:
            raise ValueError('Un mascle no pot estar alletant')
        return v

class AnimalCreate(AnimalBase):
    pass

class AnimalUpdate(AnimalBase):
    pass

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
    partos: List[PartoResponse] = []
    created_at: datetime
    updated_at: datetime

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
    """Modelo de respuesta para explotaciones"""
    stats: ExplotacioStats
    animales: List[AnimalListItem]
    
    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        arbitrary_types_allowed=True
    )

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
            date: lambda v: v.strftime("%Y-%m-%d")
        }