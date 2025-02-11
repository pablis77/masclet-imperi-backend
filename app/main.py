from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings, TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from app.api.endpoints import animals
from app.api.endpoints.dashboard import router as dashboard_router
from app.core.error_handlers import http_error_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(dashboard_router, prefix="/api/v1", tags=["dashboard"])
app.include_router(animals.router, prefix="/api/animals", tags=["animals"])

# Register Tortoise ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

# Registrar manejador de errores
app.add_exception_handler(Exception, http_error_handler)
app.add_exception_handler(RequestValidationError, http_error_handler)

@app.get("/")
async def root():
    return {"message": "Welcome to Masclet Imperi API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)