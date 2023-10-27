from pydantic import BaseModel, Extra
from pydantic import StrictStr


class OutputKeys(BaseModel):
    full_name: StrictStr = "Your Full Name"
    class Config:
        extra = Extra.forbid
