# self is used to bind objects to the method

# The absence of a TypeError in your code is due to the lack of self or cls in the method signature. The method is treated like a regular function inside the class.

# Using @staticmethod makes your intention explicit, improving readability and consistency.

# While the code works without the decorator, it's a best practice to use @staticmethod when defining methods that don't rely on an instance or the class.

# decorators are used to implement some rule.


class Car:
    __total_cars = 0  # private variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.__total_cars += 1

    def get_full_name(self):
        return (self.brand, self.model)

    @staticmethod  # add decorators though, it will work without them as well, but it's a good practice
    def get_total_cars():  # this is a static method, since it is NOT dependent on objects
        return Car.__total_cars

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electric Charge"


tesla = ElectricCar("Tesla", "Model S", "85kWH")
nissan = ElectricCar("Nissan", "Leaf", "40kWH")
nexon = Car("Tata", "Nexon")
safari = Car("Tata", "Safari")

print(Car.get_total_cars())
