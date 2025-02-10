from tortoise import fields, models
from passlib.hash import bcrypt
from datetime import datetime

class User(models.Model):
    """Modelo para usuarios del sistema"""
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(max_length=100)
    full_name = fields.CharField(max_length=50)
    is_active = fields.BooleanField(default=True)
    is_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(null=True)

    class Meta:
        table = "users"