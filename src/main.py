import nest_asyncio
from fastapi import FastAPI

from api.config import settings, logger
from api.events import startup, shutdown
from api.middlewares import calculate_process_time
from api.middlewares import generate_request_id
from api.routers import home
from api.routers import metadata
from api.routers import sample_router
from api.utils.modify_request_validator import modify_request_validator
from api.utils.modify_response_validator import modify_response_validator


nest_asyncio.apply()


app = FastAPI(
    title = "API-Template-Python",
    version = "1.0.0",
    description = "A Python based API Template built on FastAPI framework for ML and AI applications.",
    contact = {
        "name": "Animesh Bala Ani",
        "email": "animesh.ani@live.com",
        },
    root_path = settings.ROOT_PATH,
    )


startup.include_event(app, logger)
shutdown.include_event(app, logger)

calculate_process_time.calculate_process_time_middleware(app)
generate_request_id.generate_request_id_middleware(app)

app.include_router(home.router)
app.include_router(metadata.router)
app.include_router(sample_router.router)

modify_request_validator(app, logger)
modify_response_validator(app, logger)
