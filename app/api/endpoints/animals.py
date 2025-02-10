from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional, Dict, Union
from datetime import datetime
from tortoise.contrib.fastapi import HTTPNotFoundError
from app.models.animal import Animal, Estat, Genere
from app.models.animal_history import AnimalHistory
from app.schemas.animal import AnimalCreate, AnimalUpdate, AnimalResponse, AnimalDetail, ExplotacioResponse
from app.core.messages import APIMessage, MessageType, MessageResponse

router = APIRouter()

@router.post("/animals", response_model=Dict, status_code=status.HTTP_201_CREATED)
async def create_animal(animal: AnimalCreate) -> MessageResponse:
    """Crea un nuevo animal (Nueva Ficha)"""
    try:
        new_animal = await Animal.create(**animal.dict())
        return MessageResponse(
            type=MessageType.SUCCESS,
            message="Animal creado correctamente",
            data={"animal": new_animal},
            duration=3000,
            position="bottom-center"
        )
    except Exception as e:
        return MessageResponse(
            type=MessageType.ERROR,
            message=f"Error: {str(e)}",
            duration=5000,  # Errores visibles más tiempo
            position="bottom-center"
        )

@router.get("/animals", response_model=List[AnimalResponse])
async def get_animals(
    explotacio: Optional[str] = None,
    nom: Optional[str] = None
):
    """Consulta de Fichas - búsqueda por nombre o explotación"""
    query = Animal.all()
    if explotacio:
        query = query.filter(explotacio=explotacio)
    if nom:
        query = query.filter(nom=nom)
    return await query.prefetch_related('partos')

@router.get("/animals/{animal_id}", response_model=AnimalResponse)
async def get_animal(animal_id: int):
    """Obtiene detalles de un animal específico"""
    animal = await Animal.get_or_none(id=animal_id).prefetch_related('partos')
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal

@router.put("/animals/{animal_id}", response_model=AnimalResponse)
async def update_animal(animal_id: int, animal_data: AnimalUpdate):
    """Actualiza un animal y registra el histórico"""
    animal = await Animal.get_or_none(id=animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    
    # Guardar datos antiguos
    old_data = await animal.to_dict()
    
    # Actualizar
    await animal.update_from_dict(animal_data.dict(exclude_unset=True))
    await animal.save()
    
    # Registrar cambios
    new_data = await animal.to_dict()
    for field, new_value in new_data.items():
        if field in old_data and old_data[field] != new_value:
            await AnimalHistory.create(
                animal_id=animal_id,
                field_name=field,
                old_value=str(old_data[field]),
                new_value=str(new_value)
            )
    
    return animal

@router.delete("/animals/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_animal(animal_id: int):
    """Elimina un animal (solo admin)"""
    deleted = await Animal.filter(id=animal_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return {"message": "Animal eliminado correctamente"}

@router.get("/animals/{animal_id}/history")
async def get_animal_history(animal_id: int):
    """Obtiene el histórico de cambios de un animal"""
    history = await AnimalHistory.filter(animal_id=animal_id).order_by("-changed_at")
    return history

@router.get("/animals/search")
async def search_animals(
    nom: str = None, 
    explotacio: str = None
):
    """Búsqueda de animales por nombre o explotación"""
    if nom:
        return await get_animal_details(nom)
    elif explotacio:
        return await get_explotacion_animals(explotacio)
    raise HTTPException(status_code=400, detail="Se requiere nom o explotacio")

@router.get("/animals/{animal_id}/full")
async def get_animal_details(animal_id: int):
    """Obtiene detalles completos de un animal incluyendo partos"""
    animal = await Animal.get_or_none(id=animal_id).prefetch_related('partos')
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal

@router.get("/animals/{nom}")
async def get_animal_details(nom: str):
    """Obtiene ficha completa de un animal"""
    animal = await Animal.get_or_none(nom=nom).prefetch_related('partos')
    if not animal:
        raise HTTPException(status_code=404, detail="Fitxa no trobada")
    
    return {
        "general": {
            "explotacio": animal.explotacio,
            "nom": animal.nom,
            "genere": animal.genere,
            "pare": animal.pare,
            "mare": animal.mare,
            "quadra": animal.quadra,
            "cod": animal.cod,
            "num_serie": animal.num_serie,
            "dob": animal.dob,
            "estado": animal.estado,
            "alletar": animal.alletar
        },
        "partos": [{
            "fecha": parto.fecha,
            "genere": parto.genere,
            "estado": parto.estado
        } for parto in animal.partos]
    }

@router.get("/explotacions/{explotacio}")
async def get_explotacion_details(explotacio: str):
    """Obtiene lista y estadísticas de una explotación"""
    animales = await Animal.filter(explotacio=explotacio)
    
    # Estadísticas (M/H/T formato)
    stats = {
        "machos": len([a for a in animales if a.genere == "M" and a.estado != "DEF"]),
        "hembras": len([a for a in animales if a.genere == "F" and a.estado != "DEF"]),
        "terneros": len([a for a in animales if a.alletar and a.estado != "DEF"]),
        "fecha": datetime.now().strftime("%H:%M %d/%m/%Y")
    }
    
    return {
        "stats": stats,
        "animales": [{
            "nom": animal.nom,
            "cod": animal.cod,
            "dob": animal.dob,
            "genere": animal.genere,
            "estado": animal.estado,
            "alletar": animal.alletar,
            "num_partos": len(await animal.partos)
        } for animal in animales]
    }

@router.get("/explotacions/{explotacio}/pdf")
async def generate_explotacion_pdf(explotacio: str):
    """Genera PDF de la explotación"""
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
    
    data = await get_explotacion_details(explotacio)
    # TODO: Implementar generación PDF similar a la original

@router.get("/animals/{id}", response_model=Union[AnimalResponse, MessageResponse])
async def get_animal(id: int):
    """Obtiene detalles de un animal por ID"""
    animal = await Animal.get_or_none(id=id).prefetch_related('partos')
    if not animal:
        return MessageResponse(
            message="Animal no trobat",
            type=MessageType.ERROR,
            status_code=404
        )
    return animal

@router.get("/animals/by-name/{nom}", response_model=AnimalDetail)
async def get_animal_by_name(nom: str):
    """Obtiene ficha completa de un animal por nombre"""
    animal = await Animal.get_or_none(nom=nom).prefetch_related('partos')
    if not animal:
        raise HTTPException(
            status_code=404, 
            detail="Fitxa no trobada"
        )
    return AnimalDetail.from_orm(animal)

@router.get("/explotacions/{explotacio}", response_model=ExplotacioResponse)
async def get_explotacion_details(explotacio: str):
    """Obtiene lista y estadísticas de una explotación"""
    animales = await Animal.filter(explotacio=explotacio).prefetch_related('partos')
    
    stats = {
        "machos": len([a for a in animales if a.genere == Genere.M and a.estado != Estat.DEF]),
        "hembras": len([a for a in animales if a.genere == Genere.F and a.estado != Estat.DEF]),
        "terneros": len([a for a in animales if a.alletar and a.estado != Estat.DEF]),
        "fecha": datetime.now().strftime("%H:%M %d/%m/%Y")
    }
    
    return ExplotacioResponse(
        stats=stats,
        animales=[{
            "nom": animal.nom,
            "cod": animal.cod,
            "dob": animal.dob,
            "genere": animal.genere,
            "estado": animal.estado,
            "alletar": animal.alletar,
            "num_partos": len(await animal.partos)
        } for animal in animales]
    )