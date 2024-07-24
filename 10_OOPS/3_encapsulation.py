# Encapsulation in Python
class Car:
    def __init__(self, make, model):
        self.__make = make   # Private attribute
        self.__model = model # Private attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

car = Car("Toyota", "Camry")
print(car.get_make())
print(car.get_model())

car.set_make("Honda")
car.set_model("Accord")
print(car.get_make())
print(car.get_model())