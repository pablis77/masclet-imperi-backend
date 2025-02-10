# backend/app/models/animal.py
from enum import Enum
from tortoise import fields, models
from tortoise.models import Model

class Genere(str, Enum):
    MASCLE = "M"
    FEMELLA = "F"

class Estat(str, Enum):
    OK = "OK"
    FALLECIDO = "DEF"  # Cambiado a DEF para coincidir con el CSV

class Animal(Model):
    id = fields.IntField(pk=True)
    nom = fields.CharField(max_length=100, unique=True)
    cod = fields.CharField(max_length=50, unique=True, null=True)
    num_serie = fields.CharField(max_length=50, unique=True, null=True)
    alletar = fields.BooleanField(default=False)
    estado = fields.CharEnumField(Estat, default=Estat.OK)
    genere = fields.CharEnumField(Genere)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    # Campos adicionales según CSV
    explotacio = fields.CharField(max_length=100, null=True)
    pare = fields.CharField(max_length=100, null=True)
    mare = fields.CharField(max_length=100, null=True)
    quadra = fields.CharField(max_length=100, null=True)
    dob = fields.DateField(null=True)  # Date of Birth

    class Meta:
        table = "animals"

    def __str__(self):
        return f"{self.nom} ({self.genere})"