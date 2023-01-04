from unittest import TestCase, main
from python_oop.exercise.exercise_10_testing.mammal.project.mammal  import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Test", "test type", "test sound")

    def test_correct_initializing(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_make_sound_return_correct_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes test sound", result)

    def test_if_get_kingdom_returns_correct_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_get_info_returns_correct_message(self):
        result = self.mammal.info()
        self.assertEqual("Test is of type test type", result)


if __name__ == "__main__":
    main()
