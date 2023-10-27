import time
from fastapi import Request


def calculate_process_time_middleware(app):
    
    @app.middleware("http")
    async def add_calculate_process_time(request: Request, call_next):
        
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        response.headers["process-time"] = str(process_time)
        
        return response
