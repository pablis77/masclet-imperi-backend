# backend/app/models/animal.py
from tortoise import fields, models, validators
from enum import Enum
from .icons import get_animal_icon

class Genere(str, Enum):
    MASCLE = "M"
    FEMELLA = "F"

class Estado(str, Enum):
    ACTIVO = "activo"
    FALLECIDO = "fallecido"

class Animal(models.Model):
    id = fields.IntField(pk=True)
    alletar = fields.BooleanField(default=False)
    explotacio = fields.CharField(max_length=255, null=True)
    nom = fields.CharField(max_length=255, unique=True)
    genere = fields.CharEnumField(Genere, null=True)
    pare = fields.CharField(max_length=255, null=True)
    mare = fields.CharField(max_length=255, null=True)
    quadra = fields.CharField(max_length=50, null=True)
    cod = fields.CharField(max_length=50, null=True, unique=True)
    num_serie = fields.CharField(max_length=50, null=True, unique=True)
    dob = fields.DateField(null=True, description="Date of Birth")
    estado = fields.CharEnumField(Estado, default=Estado.ACTIVO)
    part = fields.DateField(null=True)
    genereT = fields.CharEnumField(Genere, null=True)
    estadoT = fields.CharEnumField(Estado, null=True)
    
    class Meta:
        table = "animals"

    def __str__(self):
        return f"{self.num_serie} - {self.nom}" if self.num_serie else self.nom

    async def save(self, *args, **kwargs):
        # Forzar valores para machos
        if self.genere == "M":
            self.alletar = False
            self.part = None
        return await super().save(*args, **kwargs)

    @property
    def icon(self) -> str:
        """Retorna el icono apropiado para el animal"""
        icon_config = get_animal_icon(
            self.genere,
            self.alletar,
            self.estado
        )
        return icon_config.icon