# classes and objects


class Car:
    def __init__(self, brand, model):  # constructor
        self.brand = brand
        self.model = model


my_car = Car("Volkswagen", "HFT")
print(my_car.brand, my_car.model)  # Volkswagen HFT


my_new_car = Car("Tata", "Safari")
print(my_new_car.brand, my_new_car.model)  # Tata Safari
