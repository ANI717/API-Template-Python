from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse


def modify_response_validator(app,
                             logger,
                             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail="internal server error: output keys doesn't match"):
    
    @app.exception_handler(ResponseValidationError)
    async def validation_exception_handler(request: Request,
                                           exc: ResponseValidationError):
        
        body = "{}: {}: {}".format(status_code, detail, str(exc))
        logger.error(body)
        return JSONResponse(
            status_code = status_code,
            content = jsonable_encoder({"body": body, "detail": exc.errors()})
            )
