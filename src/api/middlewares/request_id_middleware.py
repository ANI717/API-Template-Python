import uuid
from fastapi import Request


class Request_ID():
    REQUEST_ID = None


def request_id_middleware(app):
    
    @app.middleware("http")
    async def add_request_id(request: Request, call_next):
        
        Request_ID.REQUEST_ID = str(uuid.uuid4())
        
        response = await call_next(request)
        
        response.headers["request-id"] = Request_ID.REQUEST_ID
        
        return response
