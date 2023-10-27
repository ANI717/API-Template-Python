from fastapi import APIRouter
import datetime


deployment_date = str(datetime.datetime.now().ctime())


router = APIRouter()


@router.get("/metadata")
async def metadata():
    return {
        "deployment_date": deployment_date,
        }
