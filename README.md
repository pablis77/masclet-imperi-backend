# API Masclet Imperi

## 📋 RESUMEN EJECUTIVO

Masclet Imperi es una aplicación para la gestión de una granja de ganado bovino. Esta API proporciona el backend para la versión web del sistema, migrando desde una aplicación de escritorio existente.

### Características Principales

#### Sistema de Usuarios
- Tres niveles de acceso: administrador, editor, usuario
- Persistencia de credenciales
- Gestión de usuarios (crear, modificar, eliminar)

#### Gestión de Animales
- Registro completo de cada animal: identificación, genealogía, estado
- Seguimiento de partos y descendencia
- Búsqueda por nombre o explotación

#### Seguridad
- Autenticación requerida
- Contraseñas encriptadas
- Sistema de backups automático (limitado a 4)

### Estructura de Datos

#### Campos del Modelo Animal
- Alletar
- Explotació
- NOM
- Genere
- Pare
- Mare
- Quadra
- COD
- Nº Serie
- DOB (Date of Birth)
- Estado
- Part
- GenereT
- EstadoT

### Roles y Permisos

#### Administrador
- Acceso total
- Gestión de usuarios
- Importación masiva
- Nueva ficha

#### Editor
- Consulta
- Actualización de fichas

#### Usuario
- Solo consulta

## Tech Stack

- FastAPI
- PostgreSQL
- Tortoise ORM
- Autenticación JWT 
- Python 3.11 (en entorno conda)

## 📝 RUTINAS DIARIAS

### 🌅 INICIO DEL DÍA
```batch
# 1. Ir al directorio del proyecto
cd c:\Proyectos\claude\masclet-imperi-web\backend

# 2. Actualizar código
git pull origin main

# 3. Activar entorno conda
conda activate masclet-imperi

# 4. Actualizar dependencias si hay cambios
pip install -r requirements.txt

# 5. Iniciar servidor
uvicorn main:app --reload

# 6. Verificar en navegador
http://localhost:8000/health
http://localhost:8000/docs
```


# Antes de cualquier cambio significativo
git checkout -b feature/nueva-funcionalidad

# Después de los cambios
git add .
git commit -m "ADD: Nueva funcionalidad (mantiene funcionalidad anterior)"


### 🌙 FIN DEL DÍA
```batch
# 1. Detener servidor
Ctrl + C

# 2. Guardar cambios
git add .
git commit -m "Descripción de los cambios"
git push origin main

# 3. Desactivar entorno conda
conda deactivate
```

### ⚠️ SOLUCIÓN DE PROBLEMAS COMUNES

#### Si el servidor no arranca:
```batch
# 1. Verificar directorio correcto
cd c:\Proyectos\claude\masclet-imperi-web\backend

# 2. Verificar entorno virtual activo
.\venv\Scripts\activate

# 3. Comprobar base de datos
http://localhost:8000/health
```

> **Nota sobre PostgreSQL**: 
> - El servicio está configurado para ejecutarse automáticamente
> - No es necesario iniciar/detener manualmente
> - Solo intervenir en casos de mantenimiento

## Configuración Inicial

### Prerequisitos

- Python 3.13+
- PostgreSQL 17.2+
- Git

### Instalación

1. Crear entorno conda:
```batch
conda create -n masclet-imperi python=3.11
conda activate masclet-imperi
```

2. Crear entorno virtual e instalar dependencias:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Configuración de la Base de Datos

1. Asegúrate de estar en el directorio correcto:
```batch
cd backend
```

2. Verificar que PostgreSQL está corriendo:
```batch
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -d masclet_imperi
```

3. Configurar variables de entorno:
```batch
echo DATABASE_URL=postgres://postgres:tupassword@localhost:5432/masclet_imperi > .env
```

4. Inicializar Aerich:
```batch
aerich init -t app.database.TORTOISE_ORM
```

5. Ejecutar migraciones:
```batch
aerich init-db
```

### Iniciar el Servidor

1. Asegúrate de estar en el directorio backend:
```batch
cd c:\Proyectos\claude\masclet-imperi-web\backend
```

2. Activa el entorno virtual si no está activo:
```batch
.\venv\Scripts\activate
```

3. Inicia el servidor:
```batch
uvicorn main:app --reload
```

4. Probar la conexión:
   - Abrir http://localhost:8000/health
   - Verificar que devuelve: `{"status": "healthy", "database": "connected"}`

> **Nota**: Es importante ejecutar todos los comandos desde el directorio `backend`, no desde el directorio raíz del proyecto.

### Probar la Conexión

1. Añadir endpoint de prueba en main.py:
```python
@app.get("/health")
async def health_check():
    try:
        conn = app.state.tortoise
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": str(e)}
```

2. Iniciar el servidor:
```bash
uvicorn main:app --reload
```

3. Probar la conexión:
   - Abrir http://localhost:8000/health
   - Verificar que devuelve: `{"status": "healthy", "database": "connected"}`

## 🔑 DATOS IMPORTANTES

### Conexiones
- API Local: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- PostgreSQL: localhost:5432

### Credenciales
- Base de datos:
  - Usuario: postgres
  - Contraseña: 1234
  - BD: masclet_imperi

### Comandos Útiles
```batch
# Verificar PostgreSQL
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -d masclet_imperi

# Regenerar migraciones
aerich migrate --name add_new_field
aerich upgrade

# Actualizar dependencias
pip install -r requirements.txt
# Cambiar la línea de pydantic por:
pydantic[binary]==2.6.1
```

### Flujo de Operaciones

#### Inicio
- Verificación de directorios y archivos necesarios
- Carga de usuarios y datos
- Interfaz de login

#### Autenticación
- Verificación de credenciales
- Carga de interfaz según rol

#### Operaciones Principales
- Consulta de fichas
- Actualización de datos
- Gestión de usuarios (admin)
- Importación masiva de datos (admin)

### Características Técnicas
- Desarrollado en Python 3.13
- Interface gráfica con tkinter/ttk
- Persistencia de datos en CSV y JSON
- Sistema de backup automático
- Manejo de imágenes en base64
- Ejecutable standalone para Windows

### Seguridad y Respaldo
- Backups automáticos al modificar datos
- Límite de 4 backups mantenidos
- Encriptación de credenciales
- Validación de datos en entrada

### Validaciones y Restricciones
- Control de duplicados en importación
- Validación de formatos de datos
- Restricciones por rol de usuario
- Comprobaciones de integridad de datos

## 🚀 SIGUIENTE PASOS

### 1️⃣ CREAR RUTAS PARA ANIMALES
```batch
# Crear archivo de rutas
cd app/routes
type nul > animals.py
```

### 2️⃣ IMPLEMENTAR ENDPOINTS BÁSICOS
Los siguientes endpoints se implementarán en `app/routes/animals.py`:
- GET /animals - Listar todos los animales
- GET /animals/{id} - Obtener un animal específico
- POST /animals - Crear nuevo animal
- PUT /animals/{id} - Actualizar animal
- DELETE /animals/{id} - Eliminar animal

### 3️⃣ CONECTAR RUTAS EN MAIN.PY
```python
# Añadir en main.py
from app.routes import animals

# Añadir después de las rutas existentes
app.include_router(animals.router, prefix="/animals", tags=["animals"])
```

### 4️⃣ PROBAR LOS ENDPOINTS
1. Asegúrate que el servidor está corriendo:
```batch
uvicorn main:app --reload
```

2. Visita la documentación Swagger:
   - http://localhost:8000/docs
   - Prueba los nuevos endpoints de animales

### 5️⃣ IMPLEMENTAR AUTENTICACIÓN
- Proteger rutas con JWT
- Implementar roles de usuario
- Configurar permisos por endpoint

> **Nota**: Para detener el servidor en cualquier momento, presiona `Ctrl+C` en la terminal

### Estructura del Proyecto


# Masclet Imperi Backend

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       ├── animals.py
│   │       ├── auth.py
│   │       └── dashboard.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── error_handlers.py
│   │   └── security.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── animal.py
│   │   ├── base.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── animal.py
│   │   ├── base.py
│   │   └── user.py
│   └── services/
│       ├── __init__.py
│       └── auth.py
├── migrations/
│   └── versions/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api/
│   │   ├── __init__.py
│   │   ├── test_animals.py
│   │   └── test_auth.py
│   └── test_services/
│       ├── __init__.py
│       └── test_auth.py
├── scripts/
│   ├── backup_config.py
│   └── check_setup.py
├── .env
├── .gitignore
├── aerich.ini
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Directory Description

- `app/`: Main application package
  - `api/`: API routes and dependencies
  - `core/`: Core functionality and configuration
  - `db/`: Database configuration
  - `models/`: SQLAlchemy/Tortoise ORM models
  - `schemas/`: Pydantic models for request/response
  - `services/`: Business logic

- `migrations/`: Database migrations
- `tests/`: Test files
- `scripts/`: Utility scripts

## Development Setup

1. Crear entorno conda:
```powershell
conda create -n masclet-imperi python=3.11
conda activate masclet-imperi
```

2. Instalar dependencias:
```powershell
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```powershell
uvicorn app.main:app --reload
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🐳 Docker Setup

### Prerequisites
- Docker Desktop
- Docker Compose

### Build and Run with Docker
```bash
# Build the images
docker-compose build

# Start the services
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Commands
```bash
# Rebuild a specific service
docker-compose build api

# Restart a service
docker-compose restart api

# View running containers
docker-compose ps

# Execute commands in container
docker-compose exec api bash
```

### Environment Variables
Docker uses the following environment variables from `.env`:
- `DATABASE_URL`: PostgreSQL connection string
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name

### Docker Development Tips
- Use `volumes` to mount local code into container
- Hot reload is enabled by default
- Access logs with `docker-compose logs -f`
- Use `docker-compose down -v` to remove volumes when needed

1. Revisar contenido existente
2. Identificar dónde añadir nuevo contenido
3. AÑADIR, no reemplazar
4. Verificar que todo el contenido anterior sigue intacto
5. Documentar el cambio en git

