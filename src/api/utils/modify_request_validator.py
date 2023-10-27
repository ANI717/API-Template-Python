from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def modify_request_validator(app,
                             logger,
                             status_code=status.HTTP_400_BAD_REQUEST,
                             detail="bad request: input keys doesn't match"):
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request,
                                           exc: RequestValidationError):
        
        body = "{}: {}: {}".format(status_code, detail, str(exc))
        logger.error(body)
        return JSONResponse(
            status_code = status_code,
            content = jsonable_encoder({"body": body, "detail": exc.errors()})
            )
