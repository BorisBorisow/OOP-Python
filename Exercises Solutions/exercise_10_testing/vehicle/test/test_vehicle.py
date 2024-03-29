from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50.0, 100.0)

    def test_init(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(100.0, self.vehicle.horse_power)

    def test_drive_when_enough_fuel_subtract_needed_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_when_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100.0)
        self.assertEqual( "Not enough fuel", str(ex.exception))

    def test_refuel_when_fill_less_than_capacity_add_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(50.0)
        self.assertEqual(50.0, self.vehicle.fuel)

    def test_refuel_when_fill_more_than_capacity_raise_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(51.0)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = f"The vehicle has 100.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
        actual = self.vehicle.__str__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()