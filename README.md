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


Visita la documentación Swagger:
   - http://localhost:8000/docs
   - Prueba los nuevos endpoints de animales



> **Nota**: Para detener el servidor en cualquier momento, presiona `Ctrl+C` en la terminal

## 🔐 Usuarios y Accesos

### Base de Datos
- **Usuario**: `postgres`
- **Contraseña**: `1234`
- **Propósito**: Conexión backend y gestión BD
- **Uso**: Configuración en `.env` y `config.py`

### Usuarios Aplicación (planificado)
- 👑 **Administrador**: Acceso total
- 👨‍💼 **Coordinador**: Gestión de explotaciones
- ✏️ **Editor**: Actualización limitada
- 👤 **Usuario**: Solo consulta

> ⚠️ **Nota**: El usuario `postgres` es solo para la conexión backend-database. 
> Los usuarios de la aplicación se gestionarán a través del frontend cuando 
> se implemente el sistema de autenticación.

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

### Docker Management Scripts
```powershell
# Start containers
.\scripts\docker-manage.ps1 -Action start

# View status
.\scripts\docker-manage.ps1 -Action status

# Create backup
.\scripts\docker-manage.ps1 -Action backup
```

## 🐳 Docker Configuration
- **Container**: masclet_imperi_db (PostgreSQL 17)
- **Port**: 5432
- **Volume**: masclet_imperi_data
- **Health Check**: Enabled (10s interval)
- **Memory**: 512MB-1GB

### PostgreSQL Settings
```properties
DATABASE_URL=postgres://postgres:1234@localhost:5432/masclet_imperi
MAX_CONNECTIONS=100
SHARED_BUFFERS=256MB
ENCODING=UTF-8
```

## 🔄 Database Backup Management

### Commands
```powershell
# Create a backup
.\scripts\docker-manage.ps1 -Action backup

# Verify latest backup
.\scripts\docker-manage.ps1 -Action verify

# Verify specific backup
.\scripts\docker-manage.ps1 -Action verify -BackupFile "path/to/backup.sql"

# Restore from backup
.\scripts\docker-manage.ps1 -Action restore -BackupFile "path/to/backup.sql"

# Initialize test data
.\scripts\docker-manage.ps1 -Action init-test
```

### Features
- Automatic backup rotation (keeps last 4 backups)
- Integrity verification
- Pre-restore backup creation
- Test data initialization
- Detailed backup analysis and reporting

### Backup Location
Backups are stored in `./docker/postgres/backups/` with timestamp-based naming:
```
backup_YYYYMMDD_HHMMSS.sql
```

## 🏗️ Arquitectura del Sistema

### Componentes Implementados
- ✅ **PostgreSQL 17**: Base de datos principal
  - Contenedorizada con Docker
  - Configuración optimizada
  - Sistema de backups
- ✅ **FastAPI Backend**: 
  - Endpoints base configurados
  - Modelos Tortoise ORM
  - Validaciones básicas

### Próximas Implementaciones
- 🚧 **Redis**: Caché y sesiones
- 🚧 **ELK Stack**: Logs y monitorización
- 🚧 **React Frontend**: UI y gestión de estado

graph TD
    A[✅ Implementado] --> |PostgreSQL 17| B[Base de Datos]
    A --> |FastAPI| C[Backend Base]
    A --> |Docker| D[Contenedorización Base]
    E[🚧 En Progreso] --> |Scripts| F[Gestión Docker]
    E --> |Validaciones| G[Sistema Base]
    H[⏳ Pendiente] --> |Redis| I[Cache]
    H --> |ELK| J[Monitorización]
    H --> |React| K[Frontend]

# 🚀 Masclet Imperi - Infrastructure Documentation

## 🛠 Current Infrastructure

### Database Server
- **Type**: PostgreSQL 17
- **Container**: masclet_imperi_db
- **Status**: ✅ Running
- **Ports**: 5432:5432
- **Credentials**:
  - Database: masclet_imperi
  - User: postgres
  - Password: 1234 (development only)
  - Host: localhost

### Docker Images
- `postgres:17` (434.72MB) - Primary database
- `masclet-imperi-web-api:latest` (197MB) - API implementation
- `masclet-imperi-web-api:backup_v1` (197MB) - Backup of initial API

### Backup System
- Location: `./docker/postgres/backups/`
- Naming: `backup_YYYYMMDD_HHMMSS.sql`
- Retention: Last 4 backups
- Verification: Automatic integrity checks

### Health Monitoring
- Database healthchecks every 10s
- Automatic restart unless stopped
- Log rotation enabled (10MB max, 3 files)

## 🎯 Development Commands
```powershell
# Infrastructure Management
.\scripts\docker-manage.ps1 -Action start    # Start all services
.\scripts\docker-manage.ps1 -Action stop     # Stop all services
.\scripts\docker-manage.ps1 -Action status   # Check system status

# Backup Management
.\scripts\docker-manage.ps1 -Action backup   # Create new backup
.\scripts\docker-manage.ps1 -Action verify   # Verify latest backup
.\scripts\docker-manage.ps1 -Action restore -BackupFile "path.sql"  # Restore from backup

# Development Tools
.\scripts\docker-manage.ps1 -Action init-test  # Initialize test data
.\scripts\docker-manage.ps1 -Action clean      # Clean unused resources
```