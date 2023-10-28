from pydantic import BaseModel, Extra
from pydantic import StrictStr


class InputKeys(BaseModel):
    first_name: StrictStr
    last_name: StrictStr
    class Config:
        extra = Extra.forbid
