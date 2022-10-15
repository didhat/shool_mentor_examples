from src.base import AbstractService
from src.repo import StudentRepository
from src.exeptions import StudentNotFound


class StudentGetAwardService(AbstractService):

    def __init__(self, student_repo: StudentRepository):
        self.__student_repo = student_repo

    def handle(self, student_id: int):
        student = self.__student_repo.get_student_by_id(student_id)
        if student is None:
            raise StudentNotFound()

        if student.score >= 4:
            return "Nice award"

        if 4 >= student.score >= 3:
            return "Not bad award"

        return "Bad ass student"
