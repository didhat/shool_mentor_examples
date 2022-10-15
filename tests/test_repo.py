from unittest import TestCase
from src.repo import StudentRepository
from src.domain import Student


class TestStudentRepo(TestCase):

    def setUp(self) -> None:
        students_list = [Student(student_id=1, name="Dan", surname="Sol", score=5)]
        self.student_repo = StudentRepository(students_list)

    def test_get_one(self):
        student = self.student_repo.get_student_by_id(1)
        self.assertEqual(1, student.student_id)
        self.assertEqual("Dan", student.name)

    def test_add_one(self):
        new_student = Student(student_id=2, name="Max", surname="Payne", score=3.5)
        res = self.student_repo.add_one_student(new_student)
        student = self.student_repo.get_student_by_id(2)
        self.assertEqual(True, res)
        self.assertEqual(2, student.student_id)

    def test_delete_one(self):
        res = self.student_repo.delete_student_by_id(1)
        self.assertEqual(True, res)
        deleted_student = self.student_repo.get_student_by_id(1)
        self.assertEqual(None, deleted_student)


