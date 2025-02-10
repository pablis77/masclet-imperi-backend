import asyncio
import asyncpg
from app.database import DATABASE_URL

async def check_database():
    try:
        print("Verificando conexión a PostgreSQL...")
        conn = await asyncpg.connect(DATABASE_URL)
        
        # Verificar la versión de PostgreSQL
        version = await conn.fetchval('SELECT version()')
        print(f"Conectado a: {version}")
        
        # Verificar que podemos crear tablas
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS test_connection (
                id serial PRIMARY KEY,
                test_column varchar(50)
            )
        ''')
        print("Prueba de creación de tabla exitosa")
        
        # Limpiar tabla de prueba
        await conn.execute('DROP TABLE test_connection')
        print("Prueba completada con éxito")
        
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(check_database())