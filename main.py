from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db, close_db
from app.routes import auth_router, animals_router

app = FastAPI(title="Masclet Imperi API")

@app.on_event("startup")
async def startup_event():
    await init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

@app.get("/health")
async def health_check():
    try:
        conn = app.state.tortoise
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": str(e)}

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(animals_router, prefix="/animals", tags=["animals"])