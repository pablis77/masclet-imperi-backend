from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.messages import APIMessage, MessageType

async def http_error_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=getattr(exc, "status_code", 500),
        content=APIMessage(
            message=str(exc),
            type=MessageType.ERROR
        ).dict()
    )