from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict
from app.models.animal import Animal
from app.schemas.animal import AnimalCreate, AnimalResponse
from tortoise.exceptions import DoesNotExist

router = APIRouter()

@router.get("", response_model=None)
async def get_animals():
    """Obtener lista de todos los animales"""
    return await Animal.all()

@router.get("/{animal_id}", response_model=None)
async def get_animal(animal_id: int):
    """Obtener un animal por su ID"""
    try:
        return await Animal.get(id=animal_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail=f"Animal con ID {animal_id} no encontrado"
        )

@router.post("", response_model=None)
async def create_animal(animal: Dict = Body(...)):
    """Crear un nuevo animal"""
    return await Animal.create(**animal)

@router.put("/{animal_id}", response_model=None)
async def update_animal(animal_id: int, animal: Dict = Body(...)):
    """Actualizar un animal existente"""
    try:
        await Animal.get(id=animal_id)
        await Animal.filter(id=animal_id).update(**animal)
        return await Animal.get(id=animal_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail=f"Animal con ID {animal_id} no encontrado"
        )

@router.delete("/{animal_id}")
async def delete_animal(animal_id: int):
    """Eliminar un animal"""
    try:
        animal = await Animal.get(id=animal_id)
        await animal.delete()
        return {"message": f"Animal con ID {animal_id} eliminado"}
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail=f"Animal con ID {animal_id} no encontrado"
        )