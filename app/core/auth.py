from fastapi_jwt_auth import AuthJWT
from fastapi import Depends, HTTPException
from app.core.config import ROLES, Action, UserRole
from app.models.user import User
import bcrypt

async def authenticate_user(username: str, password: str) -> User:
    """Versión moderna del verify_credentials original"""
    user = await User.get_or_none(username=username)
    if not user or not bcrypt.checkpw(password.encode(), user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return user

async def check_permissions(
    user: User,
    required_action: Action,
    resource: str = None
) -> bool:
    """
    Verifica permisos con contexto adicional
    Args:
        user: Usuario actual
        required_action: Acción requerida
        resource: Recurso opcional (ej: 'explotacion_1')
    """
    if required_action not in ROLES.get(user.role, []):
        raise HTTPException(
            status_code=403,
            detail=f"No tienes permisos para: {required_action}"
        )

    # Verificaciones específicas por rol
    if user.role == UserRole.COORDINATOR:
        if resource and required_action == Action.GESTIONAR_EXPLOTACIONES:
            # Verificar si el coordinador tiene acceso a esta explotación
            return await check_coordinator_access(user, resource)
    
    return True