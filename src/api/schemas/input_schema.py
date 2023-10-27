from pydantic import BaseModel, Extra
from pydantic import StrictStr


class InputKeys(BaseModel):
    first_name: StrictStr = "Your First Name"
    last_name: StrictStr = "Your last Name"
    class Config:
        extra = Extra.forbid
