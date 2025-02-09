# API Masclet Imperi

Backend API for Masclet Imperi application built with FastAPI and PostgreSQL.

## Tech Stack

- FastAPI
- PostgreSQL
- Tortoise ORM
- Autenticación JWT 
- Python 3.13

## Configuración

### Prerequisitos

- Python 3.13+
- PostgreSQL 17.2+
- Git

### Instalación

1. Clona el repositorio
```bash
git clone https://github.com/pablis77/masclet-imperi-backend.git
cd masclet-imperi-backend
```

### Estructura del Proyecto

```
backend/
├── app/
│   ├── auth/
│   │   └── auth_utils.py
│   ├── models/
│   │   ├── animal.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── __init__.py
│   ├── services/
│   ├── database.py
│   └── models.py
├── database/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

### Directorios Principales

- `app/`: Paquete principal de la aplicación
  - `auth/`: Módulos relacionados con la autenticación
  - `models/`: Modelos de datos y esquemas de base de datos
  - `routes/`: Endpoints y manejadores de rutas API
  - `services/`: Lógica de negocio y servicios
- `database/`: Migraciones y scripts de base de datos
- `main.py`: Punto de entrada de la aplicación

