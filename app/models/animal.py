# backend/app/models/animal.py
from tortoise import fields, models

class Animal(models.Model):
    id = fields.IntField(pk=True)
    alletar = fields.CharField(max_length=255, null=True)
    explotacio = fields.CharField(max_length=255, null=True)
    nom = fields.CharField(max_length=255, null=True)
    genere = fields.CharField(max_length=255, null=True)
    pare = fields.CharField(max_length=255, null=True)
    mare = fields.CharField(max_length=255, null=True)
    quadra = fields.CharField(max_length=255, null=True)
    cod = fields.CharField(max_length=255, null=True)
    num_serie = fields.CharField(max_length=255, null=True)
    dob = fields.DateField(null=True)  # Date of Birth
    estado = fields.CharField(max_length=255, null=True)
    part = fields.DateField(null=True)
    genereT = fields.CharField(max_length=255, null=True)
    estadoT = fields.CharField(max_length=255, null=True)
    
    class Meta:
        table = "animals"

    def __str__(self):
        return f"{self.num_serie} - {self.nom}"