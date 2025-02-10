from tortoise import fields, models
from enum import Enum
from .animal import Genere, Estado

class Parto(models.Model):
    id = fields.IntField(pk=True)
    madre = fields.ForeignKeyField('models.Animal', related_name='partos')
    fecha = fields.DateField()
    genere_cria = fields.CharEnumField(Genere)
    estado_cria = fields.CharEnumField(Estado, default=Estado.ACTIVO)
    numero_parto = fields.IntField()  # Para mantener el orden de los partos

    class Meta:
        table = "partos"
        ordering = ["madre_id", "numero_parto"]

    def __str__(self):
        return f"Parto {self.numero_parto} de {self.madre.nom}"