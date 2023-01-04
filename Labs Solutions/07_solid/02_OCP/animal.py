import abc


class Animal(abc.ABC):

    @abc.abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow-meow"


class Dog(Animal):
    def make_sound(self):
        return "bau-bau"


class Chicken(Animal):
    def make_sound(self):
        return "peow-peow"


class Pig(Animal):
    def make_sound(self):
        return "gruh-gruh"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken(), Pig()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
