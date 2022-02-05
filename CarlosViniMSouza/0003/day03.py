# Why Python is Great: Namedtuples

# Using namedtuple is way shorter than defining a class manually:
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)

print(my_car.color)
# Output: 'red'

print(my_car.mileage)
# Output: 3812.4

print(my_car)
# OutputCar(color='red', mileage=3812.4)
