from unittest import TestCase

from src.service import StudentGetAwardService
from src.repo import StudentRepository
from src.domain import Student
from src.exeptions import StudentNotFound


class TestStudentGetAwardService(TestCase):

    def setUp(self) -> None:
        student_list = [Student(student_id=1, name="Vasya", surname="Joj", score=4),
                        Student(student_id=2, name="Petya", surname="Kek", score=3.5),
                        Student(student_id=3, name="Bad", surname="Ass", score=2.5)]

        student_repo = StudentRepository(student_list)

        self.service = StudentGetAwardService(student_repo)

    def test_get_award_great_award(self):
        award = self.service.handle(1)
        self.assertEqual("Nice award", award)

    def test_get_not_bad_award(self):
        award = self.service.handle(2)
        self.assertEqual("Not bad award", award)

    def test_get_bad_ass(self):
        award = self.service.handle(3)
        self.assertEqual("Bad ass student", award)

    def test_get_award_for_non_exist_student(self):
        with self.assertRaises(StudentNotFound):
            self.service.handle(5)
