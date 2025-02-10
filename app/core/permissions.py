from enum import Enum
from typing import List
from fastapi import Depends, HTTPException

class Action(str, Enum):
    CONSULTAR = "consultar"
    ACTUALIZAR = "actualizar"
    CREAR = "crear"
    GESTIONAR_USUARIOS = "gestionar_usuarios"

async def check_permissions(user: User, required_action: Action):
    """Versión moderna del has_permission original"""
    if required_action not in ROLES.get(user.role, []):
        raise HTTPException(status_code=403, detail="Acción no permitida")