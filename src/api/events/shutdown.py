def include_event(app, logger):
    
    @app.on_event("shutdown")
    async def shutdown_event():
        body = "application shutdown complete"
        logger.info(body)
    
    return True
