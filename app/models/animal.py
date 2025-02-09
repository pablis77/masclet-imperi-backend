# backend/app/models/animal.py
from tortoise import fields, models
from enum import Enum

class Genere(str, Enum):
    MASCLE = "M"
    FEMELLA = "F"

class Estado(str, Enum):
    ACTIVO = "activo"
    FALLECIDO = "fallecido"

class Animal(models.Model):
    id = fields.IntField(pk=True)
    alletar = fields.BooleanField(default=False)  # Cambiado a Boolean
    explotacio = fields.CharField(max_length=255, null=True)
    nom = fields.CharField(max_length=255, unique=True)  # Nombre único
    genere = fields.CharEnumField(Genere, null=True)  # Validación de género
    pare = fields.CharField(max_length=255, null=True)
    mare = fields.CharField(max_length=255, null=True)
    quadra = fields.CharField(max_length=50, null=True)
    cod = fields.CharField(max_length=50, null=True, unique=True)  # Código único si existe
    num_serie = fields.CharField(max_length=50, null=True, unique=True)  # Número de serie único si existe
    dob = fields.DateField(null=True, description="Date of Birth")
    estado = fields.CharEnumField(Estado, default=Estado.ACTIVO)
    part = fields.DateField(null=True)
    genereT = fields.CharEnumField(Genere, null=True)
    estadoT = fields.CharEnumField(Estado, null=True)
    
    class Meta:
        table = "animals"

    def __str__(self):
        return f"{self.num_serie} - {self.nom}" if self.num_serie else self.nom

    class Config:
        schema_extra = {
            "example": {
                "nom": "Test Animal",
                "explotacio": "Granja Test",
                "genere": "M",
                "num_serie": "TEST001",
                "estado": "activo"
            }
        }