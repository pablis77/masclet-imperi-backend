import os
from tortoise import Tortoise
from fastapi import FastAPI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración por defecto
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'admin123',
    'database': 'masclet_imperi',
}

DATABASE_URL = f"postgres://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Configuración de Tortoise ORM para Aerich
TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL
    },
    "apps": {
        "models": {
            "models": [
                "app.models.animal",
                "app.models.parto",
                "app.models.user",
                "aerich.models"
            ],
            "default_connection": "default",
        }
    }
}

async def init_db(app: FastAPI) -> None:
    """Inicializa la conexión a la base de datos."""
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()
        app.state.tortoise = Tortoise
    except Exception as e:
        print(f"Error inicializando la base de datos: {e}")
        raise

async def close_db() -> None:
    """Cierra la conexión a la base de datos."""
    await Tortoise.close_connections()