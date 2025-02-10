from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Dict, List, ClassVar, Any
from typing_extensions import TypedDict
from enum import Enum
from pathlib import Path

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
    # API Information
    API_NAME: str = "MASCLET IMPERI API"
    API_VERSION: str = "1.0.0"
    
    # Database Configuration
    DB_URL: str = "postgres://postgres:1234@localhost:5432/masclet_imperi"
    
    # Roles y Permisos
    ROLES: Dict[str, List[str]] = {}
    
    # Directories
    BASE_DIR: str = str(Path(__file__).resolve().parent.parent)
    DATA_DIR: str = str(Path(BASE_DIR) / "data")
    BACKUP_DIR: str = str(Path(BASE_DIR) / "backups")

    @property
    def TORTOISE_ORM(self) -> Dict[str, Any]:
        return {
            "connections": {"default": self.DB_URL},
            "apps": {
                "models": {
                    "models": ["app.models.animal", "app.models.animal_history", "aerich.models"],
                    "default_connection": "default",
                }
            },
        }
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

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

# Create settings instance
settings = Settings()