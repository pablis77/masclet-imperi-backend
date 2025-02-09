# backend/app/models/animal.py
from tortoise import fields, models

class Animal(models.Model):
    id = fields.IntField(pk=True)
    alletar = fields.CharField(max_length=50, null=True)
    explotacio = fields.CharField(max_length=255, null=True)
    nom = fields.CharField(max_length=255, unique=True)  # Nombre único
    genere = fields.CharField(max_length=50, null=True)
    pare = fields.CharField(max_length=255, null=True)
    mare = fields.CharField(max_length=255, null=True)
    quadra = fields.CharField(max_length=50, null=True)
    cod = fields.CharField(max_length=50, null=True, unique=True)  # Código único si existe
    num_serie = fields.CharField(max_length=50, null=True, unique=True)  # Número de serie único si existe
    dob = fields.DateField(null=True)  # Date of Birth
    estado = fields.CharField(max_length=50, null=True)
    part = fields.DateField(null=True)
    genereT = fields.CharField(max_length=50, null=True)
    estadoT = fields.CharField(max_length=50, null=True)
    
    class Meta:
        table = "animals"

    def __str__(self):
tudia        return f"{self.num_serie} - {self.nom}" if self.num_serie else self.nom