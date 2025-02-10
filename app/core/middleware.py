from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class MessageMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        if isinstance(response, JSONResponse):
            data = response.body.decode()
            modified_response = {
                "data": data,
                "message": None,
                "status": response.status_code
            }
            return JSONResponse(modified_response)
        return response