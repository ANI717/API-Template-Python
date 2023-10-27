from fastapi import status, HTTPException
from api.services.get_full_name import get_full_name


def generate_output(inputs,
                    logger,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="failed generating output"):
    try:
        return get_full_name(inputs)
    except Exception as exc:
        body = "{}: {}: {}".format(status_code, detail, str(exc))
        logger.error(body)
        raise HTTPException(status_code=status_code, detail=body)
