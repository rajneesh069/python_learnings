# we'll make the 'model' property readonly, i.e., once it's set, we cannot change it.


class Car:
    __total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = (
            model  # made it private, so that it's not accessible outside the class
        )
        Car.__total_cars += 1

    def get_full_name(self):
        return (self.brand, self.model)

    @staticmethod
    def get_total_cars():
        return Car.__total_cars

    def fuel_type(self):
        return "Petrol or Diesel"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electric Charge"


tesla = ElectricCar("Tesla", "Model S", "85kWH")

print(isinstance(tesla, ElectricCar))  # True
print(isinstance(tesla, Car))  # True
