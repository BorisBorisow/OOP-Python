from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance):
        drive_to_refuel = self.fuel_quantity / (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if distance <= drive_to_refuel:
            self.fuel_quantity -= needed_fuel
        return distance <= drive_to_refuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6
    MAX_CAPACITY = 0.95

    def drive(self, distance):
        drive_to_refuel = self.fuel_quantity / (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if distance <= drive_to_refuel:
            self.fuel_quantity -= needed_fuel
        return distance <= drive_to_refuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.MAX_CAPACITY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
