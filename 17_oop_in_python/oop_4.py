class Car:
    def __init__(self, model):
        self.model = model

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"Brand:{self.__brand}, Model: {self.model}"


my_car = Car("Model S")
my_car.set_brand("Tesla")
print(my_car.get_brand())
