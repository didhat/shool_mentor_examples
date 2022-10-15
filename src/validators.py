from typing import Dict

from pydantic import BaseModel, StrictStr, root_validator, ValidationError


class InputFullName(BaseModel):
    name: StrictStr
    surname: StrictStr

    class Config:
        extra = "forbid"



