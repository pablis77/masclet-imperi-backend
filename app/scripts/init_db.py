from tortoise import Tortoise, run_async
from app.models.user import User
from app.database import TORTOISE_ORM
import sys

async def init_db():
    """Inicializa la base de datos con datos por defecto"""
    try:
        print("Iniciando conexión a la base de datos...")
        await Tortoise.init(config=TORTOISE_ORM)
        
        print("Generando esquemas...")
        await Tortoise.generate_schemas(safe=True)
        
        print("Verificando usuario admin...")
        if not await User.filter(username="admin").exists():
            print("Creando usuario admin...")
            user = User(
                username="admin",
                full_name="Administrador",
                password_hash=User.hash_password("admin123"),
                is_admin=True
            )
            await user.save()
            print("Usuario administrador creado con éxito")
        else:
            print("El usuario admin ya existe")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        raise
    finally:
        print("Cerrando conexiones...")
        await Tortoise.close_connections()

if __name__ == "__main__":
    run_async(init_db())