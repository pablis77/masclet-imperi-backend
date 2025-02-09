from tortoise import Tortoise, run_async
import logging
from app.models import User, Animal

# Base PostgreSQL connection URL - Cambiado de postgresql:// a postgres://
DATABASE_URL = "postgres://postgres:1234@localhost:5432/masclet_imperi"

async def init():
    logger = logging.getLogger(__name__)
    logger.info("Intentando conectar a la base de datos...")
    try:
        await Tortoise.init(
            db_url=DATABASE_URL,
            modules={'models': ['app.models.user', 'app.models.animal']}
        )
        logger.info("Conexión establecida correctamente")
        await Tortoise.generate_schemas()
    except Exception as e:
        logger.error(f"Error al conectar a la base de datos: {str(e)}")
        raise

async def close():
    await Tortoise.close_connections()