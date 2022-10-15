from pydantic import BaseModel, StrictStr


class Student(BaseModel):
    student_id: int
    name: StrictStr
    surname: StrictStr
    score: float

