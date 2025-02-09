from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes.animals import router as animals_router

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(animals_router, prefix="/animals", tags=["animals"])

# Eventos de inicio y cierre
@app.on_event("startup")
async def startup_event():
    await init_db(app)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}