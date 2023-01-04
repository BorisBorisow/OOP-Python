from unittest import TestCase, main

# from python_oop.exercise.exercise_10_testing.student.project.student import Student
from project.student import Student


class TestStudent(TestCase):  # Test suit

    def setUp(self):
        self.student = Student("TestGuy1")
        self.student_with_course = Student("TestGuy2", {"math": ["some note"]})

    def test_initializing(self):
        self.assertEqual("TestGuy2", self.student_with_course.name)
        self.assertEqual({"math": ["some note"]}, self.student_with_course.courses)
        self.assertEqual("TestGuy1", self.student.name)
        self.assertEqual({}, self.student.courses)

    def tests_add_notes_to_existing_course(self):
        actual = self.student_with_course.enroll("math", ["note 1", "note 2"])
        expected = "Course already added. Notes have been updated."

        self.assertEqual(["some note", "note 1", "note 2"], self.student_with_course.courses["math"])
        self.assertEqual(3, len(self.student_with_course.courses["math"]))
        self.assertEqual("note 2", self.student_with_course.courses["math"][2])
        self.assertEqual("note 1", self.student_with_course.courses["math"][1])
        self.assertEqual(expected, actual)

    def test_add_notes_to_non_existing_course_without_third_param(self):
        actual = self.student.enroll("OOP", ["Polymorphism", "Design Patterns"])
        expected = "Course and course notes have been added."

        self.assertEqual(["Polymorphism", "Design Patterns"], self.student.courses["OOP"])
        self.assertEqual(expected, actual)

    def test_add_notes_to_non_existing_course_with_third_param_y(self):
        actual = self.student.enroll("OOP", ["Polymorphism", "Design Patterns"], "Y")
        expected = "Course and course notes have been added."

        self.assertEqual(["Polymorphism", "Design Patterns"], self.student.courses["OOP"])
        self.assertEqual(expected, actual)

    def test_add_new_course_without_adding_the_notes(self):
        actual = self.student.enroll("Python", ["Inheritance"], "n")
        expected = "Course has been added."

        self.assertEqual([], self.student.courses["Python"])
        self.assertEqual(expected, actual)

    def test_if_add_note_method_work_correct(self):
        actual = self.student_with_course.add_notes("math", "new note")
        expected = "Notes have been updated"

        self.assertEqual(["some note", "new note"], self.student_with_course.courses["math"])
        self.assertEqual(expected, actual)

    def test_add_note_to_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("German", ["note 1"])

        expected = "Cannot add notes. Course not found."
        self.assertEqual(expected, str(ex.exception))

    def test_leave_existing_course(self):
        actual = self.student_with_course.leave_course("math")
        expected = "Course has been removed"

        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual(expected, actual)

    def test_leave_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")

        expected = "Cannot remove course. Course not found."
        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    main()
