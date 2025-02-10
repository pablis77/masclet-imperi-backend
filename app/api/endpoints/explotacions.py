@router.get("/explotacions/{id}/stats")
async def get_explotacion_stats(id: str):
    """Estadísticas y listado de explotación"""