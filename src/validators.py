from pydantic import BaseModel, StrictInt


class InputForTakeAward(BaseModel):
    student_id: StrictInt

    class Config:
        extra = "forbid"

