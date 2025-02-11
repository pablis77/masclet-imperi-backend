from fastapi import APIRouter, HTTPException
from app.models.animal import Animal, Estat, Genere
from app.schemas.animal import ExplotacioStats
from typing import Dict
from datetime import datetime, timedelta
import logging

router = APIRouter()

@router.get("/")
async def read_dashboard():
    return {"status": "dashboard operational"}

@router.get("/dashboard/resumen")
async def obtener_resumen():
    """
    Obtiene estadísticas básicas para el dashboard
    """
    total_animales = await Animal.all().count()
    activos = await Animal.filter(estado=Estat.ACTIU).count()
    
    return {
        "total_animales": total_animales,
        "animales_activos": activos,
        "porcentaje_activos": round(activos/total_animales * 100 if total_animales > 0 else 0, 2)
    }

@router.get("/dashboard/stats", response_model=Dict)
async def get_dashboard_stats():
    try:
        # Verificar que hay conexión con la base de datos
        if not await Animal.exists():
            return {
                "status": "success",
                "data": {
                    "total_animales": 0,
                    "resumen": {
                        "activos": 0,
                        "porcentaje_activos": 0
                    },
                    "por_genero": {
                        "toros": 0,
                        "vacas": 0
                    }
                }
            }

        total = await Animal.all().count()
        activos = await Animal.filter(estado=Estat.ACTIU).count()
        
        return {
            "status": "success",
            "data": {
                "total_animales": total,
                "resumen": {
                    "activos": activos,
                    "porcentaje_activos": round((activos/total * 100) if total > 0 else 0, 2)
                },
                "por_genero": {
                    "toros": await Animal.filter(genere=Genere.MASCLE).count(),
                    "vacas": await Animal.filter(genere=Genere.FEMELLA).count()
                }
            }
        }
    except Exception as e:
        logging.error(f"Error en dashboard stats: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error obteniendo estadísticas: {str(e)}"
        )

@router.get("/dashboard/recientes", response_model=Dict)
async def get_recent_activity():
    """
    Obtiene la actividad reciente:
    - Últimos animales registrados
    - Cambios de estado recientes
    """
    una_semana = datetime.now() - timedelta(days=7)
    
    return {
        "nuevos_registros": await Animal.filter(
            created_at__gte=una_semana
        ).count(),
        "ultimos_animales": await Animal.filter(
            created_at__gte=una_semana
        ).order_by("-created_at").limit(5).values(
            "id", "nom", "genere", "created_at"
        )
    }

@router.get("/stats", response_model=ExplotacioStats)
async def get_dashboard_stats():
    return {
        "total": 0,
        "machos": 0,
        "hembras": 0,
        "terneros": 0,
        "fecha": "2024-02-11T00:00:00"
    }