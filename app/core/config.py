from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Dict, List, ClassVar, Any
from typing_extensions import TypedDict
from enum import Enum
from pathlib import Path
from functools import lru_cache

class UserRole(str, Enum):
    ADMIN = "administrador"
    COORDINATOR = "coordinador"
    EDITOR = "editor"
    USER = "usuario"

class Action(str, Enum):
    CONSULTAR = "consultar"
    ACTUALIZAR = "actualizar"
    CREAR = "crear"
    GESTIONAR_USUARIOS = "gestionar_usuarios"
    GESTIONAR_EXPLOTACIONES = "gestionar_explotaciones"
    IMPORTAR_DATOS = "importar_datos"
    VER_ESTADISTICAS = "ver_estadisticas"
    EXPORTAR_DATOS = "exportar_datos"

class UIStyle(TypedDict):
    color: str
    duration: int

class UIStyles(TypedDict):
    success: UIStyle
    error: UIStyle
    info: UIStyle

class Settings(BaseSettings):
    DATABASE_URL: str
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Masclet Imperi"
    SECRET_KEY: str = "your-secret-key"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

settings = Settings()

# Tortoise ORM Configuration
TORTOISE_ORM: Dict[str, Any] = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": "masclet_imperi",
                "host": "localhost",
                "password": "1234",
                "port": 5432,
                "user": "postgres",
                "min_size": 1,
                "max_size": 5
            }
        }
    },
    "apps": {
        "models": {
            "models": ["app.models.animal", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
}

# UI Styles como constante global
UI_STYLES = {
    'success': {'color': '#28a745', 'duration': 3000},
    'error': {'color': '#dc3545', 'duration': 5000},
    'info': {'color': '#17a2b8', 'duration': 3000}
}

# Roles como constante global
ROLES = {
    UserRole.ADMIN: [
        Action.CONSULTAR,
        Action.ACTUALIZAR,
        Action.CREAR,
        Action.GESTIONAR_USUARIOS,
        Action.GESTIONAR_EXPLOTACIONES,
        Action.IMPORTAR_DATOS,
        Action.VER_ESTADISTICAS,
        Action.EXPORTAR_DATOS
    ],
    UserRole.COORDINATOR: [
        Action.CONSULTAR,
        Action.ACTUALIZAR,
        Action.CREAR,
        Action.GESTIONAR_EXPLOTACIONES,
        Action.VER_ESTADISTICAS,
        Action.EXPORTAR_DATOS
    ],
    UserRole.EDITOR: [
        Action.CONSULTAR,
        Action.ACTUALIZAR,
        Action.VER_ESTADISTICAS
    ],
    UserRole.USER: [
        Action.CONSULTAR
    ]
}

@lru_cache()
def get_settings() -> Settings:
    return Settings()

# Create settings instance
settings = get_settings()