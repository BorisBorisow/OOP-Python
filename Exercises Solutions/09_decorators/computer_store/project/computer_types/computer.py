from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer, model, processor, ram, price):
        self.manufacturer = manufacturer
        self.model = None
        self.ram = None
        self.price = 0

    @property
    def manufacture(self):
        return self.__manufacturer

    @manufacture.setter
    def manufacture(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if self.model == "":
            return ValueError("Model name cannot be empty.")
        self.__model = value
