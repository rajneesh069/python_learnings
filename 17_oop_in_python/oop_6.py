class Car:
    __num_of_cars = (
        0  #  a static property, property of a class and NOT of an instance/object
    )

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.num_of_cars += 1, this will not do anything because it's an instance level attribute, while the changes we want are on class level hence we do Car.num_of_cars+=1, that changes it on the class level. Much like, human class and human population as an attribute which is independent of instances and is universal for the whole class.
        Car.__num_of_cars += 1

    def full_name(self):
        return (self.brand, self.model)

    def fuel_type(self):
        return "Petrol or Diesel"

    def get_total_cars():  # pass 'self' only when that definition/function is being called through some object/instance of the class, otherwise we'll get the error that 'self' has not been provided because when we call it using objects Python passes the object as 'self' internally
        return Car.__num_of_cars


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


safari = Car("Tata", "Safari")
nexon = Car("Tata", "Nexon")
tesla = ElectricCar("Tesla", "Model S", "85kWH")
bmw = Car("BMW", "E81")
ElectricCar(
    "Nissan", "Leaf", "40kWh"
)  # we aren't registering it in an object, but an object get's instantiated for sure

print(
    Car.get_total_cars()
)  # returns the total number of cars(electric and normal created, electric because it calls the super constructor)
