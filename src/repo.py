from typing import List

from src.base import AbstractRepository
from src.domain import Student


class StudentRepository(AbstractRepository):

    def __init__(self, student_collection: List[Student]):
        self._collection: List[Student] = student_collection

    def _get_one(self, student_id: int):
        for student in self._collection:
            if student.student_id == student_id:
                return student
        return

    def _add_one(self, student: Student):
        self._collection.append(student)

    def _delete_one(self, student_id: int):
        for index, student in enumerate(self._collection):
            if student.student_id == student_id:
                del self._collection[index]
                return True
        return

    def get_student_by_id(self, student_id: int):
        student = self._get_one(student_id)
        return student

    def delete_student_by_id(self, student_id: int):
        res = self._delete_one(student_id)
        return res

    def add_one_student(self, student: Student):
        self._add_one(student)
        return True

