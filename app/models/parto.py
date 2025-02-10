from tortoise import fields
from tortoise.models import Model
from .animal import Genere, Estat

class Parto(Model):
    id = fields.IntField(pk=True)
    animal = fields.ForeignKeyField('models.Animal', related_name='partos')
    fecha = fields.DateField()
    genere_cria = fields.CharEnumField(Genere)
    estado_cria = fields.CharEnumField(Estat, default=Estat.ACTIU)
    numero_parto = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "partos"

    def __str__(self):
        return f"Parto {self.numero_parto} de {self.animal.nom}"