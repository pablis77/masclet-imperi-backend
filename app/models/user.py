from tortoise import fields, models
from enum import Enum
import bcrypt
from typing import Optional

class UserRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    USER = "usuari"

class User(models.Model):
    """Modelo para usuarios del sistema"""
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=128)
    role = fields.CharEnumField(UserRole, default=UserRole.USER)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            self.password_hash.encode('utf-8')
        )

    @classmethod
    async def hash_password(cls, password: str) -> str:
        return bcrypt.hashpw(
            password.encode('utf-8'), 
            bcrypt.gensalt()
        ).decode('utf-8')

    class Meta:
        table = "users"