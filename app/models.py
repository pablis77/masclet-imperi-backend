from tortoise.models import Model
from tortoise import fields

class ExampleModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "example_model"