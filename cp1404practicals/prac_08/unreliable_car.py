"""
CP1404/CP5632 Practical
Taxi class
"""
from prac_08.car import Car
import random



class UnreliableCar(Car):
    """Specialised version of a Car that includes car reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {} percent chance of working".format(super().__str__(),self.reliability)

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven. Only drive at all if rand_num < reliability.
        """

        if float(random.randint(0, 100)) < self.reliability:

            super().drive(distance)
        else:
            distance = 0

        return distance

        return distance
