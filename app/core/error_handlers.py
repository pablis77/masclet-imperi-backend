from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError

async def http_error_handler(
    request: Request, 
    exc: Union[Exception, RequestValidationError]
) -> JSONResponse:
    if isinstance(exc, RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )