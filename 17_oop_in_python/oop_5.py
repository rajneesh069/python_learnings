class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return (self.brand, self.model)

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


safari = Car("Tata", "Safari")
tesla_car = ElectricCar("Tesla", "Model S", "85kWH")
print(safari.fuel_type())
print(tesla_car.fuel_type())
