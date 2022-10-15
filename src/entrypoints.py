from flask import Flask, request
from pydantic import ValidationError
from src.validators import InputForTakeAward
from src.domain import Student
from src.repo import StudentRepository
from src.service import StudentGetAwardService
from src.exeptions import StudentNotFound

app = Flask(__name__)

student_list = [Student(student_id=1, name="Vasya", surname="Joj", score=4),
                Student(student_id=2, name="Petya", surname="Kek", score=3.5),
                Student(student_id=3, name="Bad", surname="Ass", score=2.5)]


@app.route("/get_student_award", methods=["POST"])
def get_award():
    params = request.json
    try:
        params = InputForTakeAward(**params)
    except ValidationError:
        return {"error": "ValidationError"}, 400

    student_repo = StudentRepository(student_list)
    service = StudentGetAwardService(student_repo)
    try:
        student_award = service.handle(params.student_id)
    except StudentNotFound:
        return {"error": "StudentNotFound"}, 404
    return {"data": {
        "student_id": params.student_id,
        "award": student_award
    }}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
