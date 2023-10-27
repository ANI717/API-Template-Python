from fastapi import APIRouter, status
from api.config import logger
from api.schemas import input_schema, output_schema
from api.utils.object_to_dict import object_to_dict
from api.utils.generate_output import generate_output


router = APIRouter()


@router.post("/sample", response_model=output_schema.OutputKeys)
async def sample_router(inputs: input_schema.InputKeys) -> output_schema.OutputKeys:
    
    inputs = object_to_dict(inputs,
                            logger,
                            status.HTTP_500_INTERNAL_SERVER_ERROR,
                            "failed generating output",
                            True)
    
    output = generate_output(inputs,
                             logger,
                             status.HTTP_500_INTERNAL_SERVER_ERROR,
                             "failed generating output")
    
    logger.error("Success")
    return output
