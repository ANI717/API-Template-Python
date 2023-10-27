def include_event(app, logger):
    
    @app.on_event("startup")
    async def startup_event():
        body = "application startup complete"
        logger.info(body)
    
    return True
