from typing import Dict, List
from datetime import date
from tortoise.transactions import atomic
from app.models.animal import Animal
from app.models.parto import Parto
from fastapi import HTTPException

@atomic()
async def import_animal_with_partos(data: dict) -> Animal:
    """
    Importa un animal y sus partos desde el CSV.
    Args:
        data (dict): Datos del animal y posible parto
    Returns:
        Animal: Instancia del animal creado/actualizado
    Raises:
        HTTPException: Si hay errores de validación
    """
    try:
        # Validar género
        if data.get('genere') == 'M' and (data.get('part') or data.get('alletar')):
            raise HTTPException(
                status_code=400,
                detail="Los machos no pueden tener partos ni amamantar"
            )

        # Datos básicos del animal (sin info de partos)
        animal_data = {
            k: v for k, v in data.items() 
            if k not in ['part', 'genereT', 'estadoT']
        }
        
        # Buscar o crear animal
        animal = await get_or_create_animal(animal_data)

        # Procesar parto si existe
        if data.get('part'):
            await add_parto(animal, {
                'fecha': data['part'],
                'genere_cria': data['genereT'],
                'estado_cria': data['estadoT']
            })

        return animal

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error importando animal: {str(e)}"
        )

async def get_or_create_animal(data: Dict) -> Animal:
    """Busca o crea un animal por num_serie o nom"""
    existing_animal = None
    
    if data.get('num_serie'):
        existing_animal = await Animal.filter(num_serie=data['num_serie']).first()
    
    if not existing_animal and data.get('nom'):
        existing_animal = await Animal.filter(nom=data['nom']).first()
    
    if existing_animal:
        # Actualizar datos si es necesario
        for key, value in data.items():
            setattr(existing_animal, key, value)
        await existing_animal.save()
        return existing_animal
    
    return await Animal.create(**data)

async def add_parto(animal: Animal, parto_data: Dict) -> Parto:
    """Añade un nuevo parto al historial del animal"""
    # Verificar que es hembra
    if animal.genere == 'M':
        raise HTTPException(
            status_code=400,
            detail="No se pueden añadir partos a un macho"
        )
    
    # Obtener último número de parto
    ultimo_parto = await Parto.filter(madre=animal).order_by('-numero_parto').first()
    numero_parto = (ultimo_parto.numero_parto + 1) if ultimo_parto else 1

    # Verificar que la fecha es posterior al último parto
    if ultimo_parto and parto_data['fecha'] <= ultimo_parto.fecha:
        raise HTTPException(
            status_code=400,
            detail="La fecha del parto debe ser posterior al último parto registrado"
        )

    return await Parto.create(
        madre=animal,
        numero_parto=numero_parto,
        **parto_data
    )