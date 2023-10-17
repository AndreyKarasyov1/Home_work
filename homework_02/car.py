"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = 0

    def set_engine(self, engine):
        self.engine = engine
