from tortoise import Tortoise
from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener URL de la base de datos desde variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Configuración de Tortoise ORM para Aerich
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user", "app.models.animal", "aerich.models"],  # Actualizado
            "default_connection": "default",
        },
    },
}

async def init_db(app: FastAPI) -> None:
    """Inicializa la conexión a la base de datos."""
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={
            'models': [
                'app.models.user',
                'app.models.animal',
                'aerich.models'
            ]
        }
    )
    # Genera los esquemas si no existen
    await Tortoise.generate_schemas()
    
    # Guarda la instancia de Tortoise en el estado de la app
    app.state.tortoise = Tortoise

async def close_db() -> None:
    """Cierra la conexión a la base de datos."""
    await Tortoise.close_connections()