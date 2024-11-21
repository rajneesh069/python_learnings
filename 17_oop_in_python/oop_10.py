# To understand more read README.md(last section)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Battery:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_capacity, horsepower):
        # Explicitly call the constructors of the parent classes
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_capacity)
        Engine.__init__(self, horsepower)

    def fuel_type(self):
        return "Electric Charge"


# Creating an ElectricCar instance
tesla = ElectricCar("Tesla", "Model S", "85kWH", 450)
print(f"Brand: {tesla.brand}, Model: {tesla.model}")
print(f"Battery Capacity: {tesla.battery_capacity}")
print(f"Horsepower: {tesla.horsepower}")
