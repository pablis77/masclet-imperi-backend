from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from typing import List, Dict
import pandas as pd
import shutil
from datetime import datetime
import io
from app.models.animal import Animal, Genere, Estat
from app.core.config import BACKUP_DIR

router = APIRouter()

REQUIRED_COLUMNS = [
    'Alletar', 'explotació', 'NOM', 'Genere', 'Pare', 'Mare', 
    'Quadra', 'COD', 'Nº Serie', 'DOB', 'Estado', 'part', 
    'GenereT', 'EstadoT'
]

async def create_backup():
    """Crear backup de la base de datos"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_{timestamp}.json"
    animals = await Animal.all()
    # TODO: Implementar backup real
    return backup_file

@router.post("/imports/preview")
async def preview_import(file: UploadFile = File(...)) -> Dict:
    """Preview de los datos a importar"""
    try:
        contents = await file.read()
        df = pd.read_csv(
            io.StringIO(contents.decode('iso-8859-1')),
            sep=';',
            na_filter=False,
            skiprows=1
        )
        df.columns = REQUIRED_COLUMNS

        return {
            "total_records": len(df),
            "sample_data": df.head(5).to_dict('records'),
            "columns_found": df.columns.tolist()
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error al procesar archivo: {str(e)}"
        )

@router.post("/imports/process")
async def process_import(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
) -> Dict:
    """Procesa la importación masiva de datos"""
    try:
        # Crear backup
        backup_file = await create_backup()
        
        # Leer CSV
        contents = await file.read()
        df = pd.read_csv(
            io.StringIO(contents.decode('iso-8859-1')),
            sep=';',
            na_filter=False,
            skiprows=1
        )
        df.columns = REQUIRED_COLUMNS

        # Procesar registros
        for _, row in df.iterrows():
            animal_data = {
                "nom": row["NOM"],
                "explotacio": row["explotació"],
                "genere": Genere.FEMELLA if row["Genere"] == "F" else Genere.MASCLE,
                "cod": row["COD"],
                "num_serie": row["Nº Serie"],
                "pare": row["Pare"],
                "mare": row["Mare"],
                "quadra": row["Quadra"],
                "estado": Estat.OK if row["Estado"] == "OK" else Estat.FALLECIDO,
                "alletar": True if row["Alletar"].lower() == "si" else False
            }
            
            await Animal.create(**animal_data)

        return {
            "status": "success",
            "records_processed": len(df),
            "backup_file": backup_file
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error en la importación: {str(e)}"
        )