import unittest

from car import Car
from vehicle import Vehicle
from motorcycle import Motorcycle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'RAV4', 2009)
        self.motorcycle = Motorcycle('Yamaha', 'MT-07', 2015)

    def test_car_is_instance_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))  #isinstance () возвращает True, если объект является экземпляром указанного класса или подкласса этого класса.

    def test_four_wheel_car(self):
        self.assertEqual(self.car.getNumWheels(), 4)  # assertEqual для проверки равенства двух значений

    def test_two_wheel_motorcycle(self):
        self.assertEqual(self.motorcycle.getNumWheels(), 2)

    def test_car_speed(self):
        self.car.testDrive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed(self):
        self.motorcycle.testDrive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park_mode_after_test_drive(self):
        self.car.testDrive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park_mode_after_test_drive(self):
        self.motorcycle.testDrive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
