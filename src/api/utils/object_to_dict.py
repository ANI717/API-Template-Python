from fastapi import status, HTTPException


def object_to_dict(data,
                    logger,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="failed generating output",
                    exclude_none=False):
    try:
        return data.dict(exclude_none=exclude_none)
    except Exception as exc:
        body = "{}: {}: {}".format(status_code, detail, str(exc))
        logger.error(body)
        raise HTTPException(status_code=status_code, detail=body)
