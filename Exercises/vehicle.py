import math


class NotEnoughFuelError(Exception):
    pass


class Car:

    # Don't change this code!
    def __init__(self, fuel, efficiency):
        """ (Car, int, int) -> NoneType

        fuel is an int specifying the starting amount of fuel.
        efficiency is an int specifying how much fuel the car takes
        to travel 1 unit of distance.

        Initialize a new car with an amount of fuel and a fuel efficiency.
        The car's starting position is (0,0).
        """

        self.fuel = fuel
        self.efficiency = efficiency
        self.pos_x = 0
        self.pos_y = 0

    def move(self, new_x, new_y):
        """ (Car, int, int) -> NoneType

        Move the car from its old position to (new_x, new_y).
        Reduce the car's fuel depending on its efficiency and how far it
        travelled.

        If there isn't enough fuel to reach (new_x, new_y),
        do not change car's position or fuel level.
        Instead, raise NotEnoughFuelError.

        Remember that the car can only travel horizontally and vertically!
        """
        newfuel = self.fuel - (new_x + new_y)

        if newfuel >= 0:
            self.pos_x = self.pos_x + new_x
            self.pos_y = self.pos_y + new_y
            self.fuel = newfuel

        else:
            raise NotEnoughFuelError


class HoverCar(Car):

    def __init__(self, fuel, efficiency, hover_fuel):
        """ (HoverCar, int, int, int) -> NoneType

        hover_fuel is an int specifying the starting amount of hover fuel.

        Initialize a new HoverCar.
        """
        Car.__init__(self, fuel, efficiency)
        self.hover_fuel = hover_fuel

    def move(self, new_x, new_y):
        """ (HoverCar, int, int)

        Move the hover car according to the description in the exercise.
        Remember that hover cars try using regular fuel first,
        and only use hover fuel if there isn't enough regular fuel.

        Be sure to follow the implementation guidelines for full marks!
        """

        try:
            Car.move
        except:
            NotEnoughFuelError

        newhover = self.hover_fuel - math.sqrt((new_x ** 2) + (new_y ** 2))

        if newhover >= 0:
            self.hover_fuel = newhover
            self.pos_x = self.pos_x + new_x
            self.pos_y = self.pos_y + new_y

        else:
            raise NotEnoughFuelError
