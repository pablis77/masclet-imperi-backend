# backend/app/models/animal.py
from tortoise.models import Model
from tortoise import fields

class Animal(Model):
    id = fields.IntField(pk=True)
    alletar = fields.CharField(max_length=255, null=True)
    explotacio = fields.CharField(max_length=255, null=True)
    nom = fields.CharField(max_length=255, unique=True, index=True)
    genere = fields.CharField(max_length=255, null=True)
    pare = fields.CharField(max_length=255, null=True)
    mare = fields.CharField(max_length=255, null=True)
    quadra = fields.CharField(max_length=255, null=True)
    cod = fields.CharField(max_length=255, null=True)
    num_serie = fields.CharField(max_length=255, null=True)
    dob = fields.DateField(null=True)
    estado = fields.CharField(max_length=255, null=True)
    part = fields.DateField(null=True)
    genereT = fields.CharField(max_length=255, null=True)
    estadoT = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "animals"