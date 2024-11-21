# [Based on `oop_6.py` and beyond](/17_oop_in_python/oop_6.py)

- ChatGPT has been used to generate proper notes, everything is checked though. Also, sometimes Python's Garbage Collector can take time in clearing the memory hence sometimes(not generally) so values retrieved from memory can be shown wrong values in terminal.

- Instance means object only.

---

## Question 1: Why am I getting `0` when I call `self.num_of_cars` but `4` when I use `Car.num_of_cars` in the `__init__` method of the `Car` class?

### **Answer:**

To understand why you're observing these different behaviors, we need to dive into the difference between **instance attributes** and **class attributes** in Python, and the nuances of how they are accessed and modified.

### **Instance vs Class Attributes**:

1. **Instance Attributes**: These are attributes that are unique to each instance (or object) of the class. They are typically initialized inside the `__init__` method using `self`, and each instance of the class has its own copy of these attributes.

2. **Class Attributes**: These are shared across all instances of the class. They are defined at the class level (not inside `__init__`) and can be accessed and modified using the class name or any instance of the class. The value of a class attribute is shared by all instances unless explicitly overridden at the instance level.

### **What's Happening in Your Code**:

In your code, the variable `num_of_cars` is defined as a **class attribute**, but you're mistakenly modifying it as an instance attribute inside the `__init__` method by referencing `self.num_of_cars`. This creates an instance-level attribute with the same name (`num_of_cars`), but it does **not** affect the class-level attribute. That's why when you print `Car.num_of_cars`, you get the correct value, as it accesses the class-level variable directly.

#### **Code Walkthrough**:

```python
class Car:
    num_of_cars = 0  # This is a class attribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.num_of_cars += 1  # This creates an instance attribute, not modifying the class attribute.
        # To modify the class-level attribute, you need to use Car.num_of_cars, not self.num_of_cars.

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

# Creating instances
safari = Car("Tata", "Safari")
nexon = Car("Tata", "Nexon")

print(Car.num_of_cars)  # Correctly prints 2
```

**Explanation**:

- When you create instances `safari` and `nexon`, Python looks for `num_of_cars` inside the `__init__` method and sees `self.num_of_cars`. Since it's not defined previously, it treats it as an instance attribute. So, the change only affects the instance of `num_of_cars` and does not touch the class-level variable `Car.num_of_cars`.
- When you directly access `Car.num_of_cars`, you are accessing the class-level variable, which gets incremented as expected.

### **Best Practice**:

To avoid this confusion, always be clear about whether you want to modify **instance** attributes or **class** attributes:

- If you want to modify a class attribute, **use the class name** (`Car.num_of_cars`), not `self`.
- If you want to modify an instance attribute, you should only use `self`.

#### **Improved Code**:

```python
class Car:
    num_of_cars = 0  # Class-level attribute, shared across all instances

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.num_of_cars += 1  # Use Car to modify the class attribute

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @classmethod
    def get_total_cars(cls):
        return cls.num_of_cars  # Access the class attribute correctly

# Create instances
safari = Car("Tata", "Safari")
nexon = Car("Tata", "Nexon")
tesla = Car("Tesla", "Model S")

# Access total cars using the class method
print(Car.get_total_cars())  # Output will be 3
```

#### Key Takeaways:

- **Instance attributes** are specific to each object, and each object has its own copy.
- **Class attributes** are shared among all instances, and changes affect all instances.
- When you want to modify a class attribute, use `ClassName.attribute_name` rather than `self.attribute_name`.

---

## Question 2: Why do I get the following error when I pass `self` as an argument to `get_total_cars()` but not in the other methods I defined, and how can I fix this?

Error:

```
TypeError: Car.get_total_cars() missing 1 required positional argument: 'self'
```

### **Answer**:

This error happens because you're defining the `get_total_cars` method as an **instance method**, but you're trying to call it on the class itself (`Car.get_total_cars()`), not on an instance of the class.

### **Key Concepts**:

- **Instance Methods**: These methods are intended to operate on an instance (i.e., an object). The first argument (`self`) refers to the instance itself. When you call an instance method, Python automatically passes the instance as the first argument (`self`).

- **Class Methods**: These methods are intended to operate on the class itself, not on instances. The first argument (`cls`) refers to the class itself. Class methods are defined using the `@classmethod` decorator. You can call class methods directly on the class (e.g., `ClassName.method()`).

### **What’s Going Wrong in Your Code**:

Since you defined `get_total_cars(self)` as an instance method, Python expects it to be called on an instance (i.e., `car_instance.get_total_cars()`), not on the class itself. When you call it on the class directly (`Car.get_total_cars()`), Python doesn't know what `self` refers to, and thus it raises the error.

### **How to Fix It**:

To fix this issue, you should define `get_total_cars` as a **class method** using the `@classmethod` decorator. This allows it to be called on the class itself without requiring an instance, and it will receive the class (`cls`) as its first argument instead of `self`.

### **Corrected Code**:

```python
class Car:
    __num_of_cars = 0  # Private class attribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.__num_of_cars += 1  # Increment the class-level attribute

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @classmethod  # Using the class method decorator
    def get_total_cars(cls):
        return cls.__num_of_cars  # Access the class-level variable using 'cls'

# Create instances
safari = Car("Tata", "Safari")
nexon = Car("Tata", "Nexon")
tesla = Car("Tesla", "Model S")
bmw = Car("BMW", "E81")

# Call the class method using the class itself
print(Car.get_total_cars())  # Output: 4
```

### **Detailed Explanation**:

1. **Instance Methods**: Methods that take `self` as the first argument, representing an individual instance of the class. They should be called using an object, e.g., `car.get_total_cars()`.
2. **Class Methods**: Methods that take `cls` as the first argument, representing the class itself. They should be called using the class name, e.g., `Car.get_total_cars()`. The `@classmethod` decorator is used to define such methods.

3. **Best Practice**: If a method doesn't need to access or modify instance-specific data (i.e., attributes tied to individual objects), it should be defined as a class method. This allows you to call it without needing to instantiate an object, and it's often more efficient for operations related to the class as a whole (e.g., keeping track of the total number of cars).

### **Key Takeaways**:

- Use `self` for instance methods, which operate on specific instances.
- Use `cls` for class methods, which operate on the class itself and should be called directly on the class.
- Decorate methods with `@classmethod` when they are intended to modify or access class-level attributes, not instance-level attributes.

---

## Additional Code Example for Practice:

### **Scenario: Car vs ElectricCar (Inheritance and Class Methods)**

```python
class Car:
    __num_of_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.__num_of_cars += 1

    def full_name(self):
        return f"{self.brand} {self.model}"

    @classmethod
    def get_total_cars(cls):
        return cls.__num_of_cars

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

#

 Create car and electric car instances
car1 = Car("Toyota", "Corolla")
car2 = ElectricCar("Tesla", "Model 3", "75kWh")
car3 = ElectricCar("Nissan", "Leaf", "40kWh")

# Call the class method to get total number of cars
print(Car.get_total_cars())  # Output: 3

# Call the method on the subclass (ElectricCar)
print(ElectricCar.get_total_cars())  # Output: 3 (same as Car, because it's shared)
```

**Explanation**:

- Both `Car` and `ElectricCar` inherit from `Car`. When we call `ElectricCar.get_total_cars()`, it still accesses the `__num_of_cars` class attribute from the `Car` class.
- **Best Practice**: The class method `get_total_cars` works across the entire class hierarchy, meaning it correctly counts cars even if they are instances of subclasses.

# [**Multiple Inheritance, MRO, and `super()` in Python**](/17_oop_in_python/oop_10.py)

### **1. Why Do We Need to Pass the Parent Class as an Argument?**

When using multiple inheritance in Python, the constructors of parent classes might require arguments. To ensure all parent classes are initialized correctly, arguments need to be forwarded explicitly or dynamically using `super()`.

#### **Code Example: Conflict with `super()`**

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        print("Car initialized")

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        print("Battery initialized")

class ElectricCar(Car, Battery):
    def __init__(self, brand, capacity):
        # Passing arguments directly to parent constructors
        Car.__init__(self, brand)  # Explicitly call Car constructor
        Battery.__init__(self, capacity)  # Explicitly call Battery constructor
        print("ElectricCar initialized")

ec = ElectricCar("Tesla", "85kWH")
```

#### **Output**

```
Car initialized
Battery initialized
ElectricCar initialized
```

Here, both constructors are explicitly called. This works fine but is **error-prone** because if the class hierarchy changes or more parent classes are added, you would need to update these calls manually.

---

### **2. How Does `super()` Work with Multiple Inheritance?**

`super()` dynamically resolves which class constructor or method to call next, based on the **Method Resolution Order (MRO)**. It simplifies handling multiple inheritance and ensures all parent classes are initialized without redundancy.

#### **Refactored Code with `super()`**

```python
class Car:
    def __init__(self, brand, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Pass remaining arguments down the MRO
        self.brand = brand
        print("Car initialized")

class Battery:
    def __init__(self, capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = capacity
        print("Battery initialized")

class ElectricCar(Car, Battery):
    def __init__(self, brand, capacity):
        super().__init__(brand, capacity)  # Pass all arguments to `super()`
        print("ElectricCar initialized")

ec = ElectricCar("Tesla", "85kWH")
```

#### **Output**

```
Battery initialized
Car initialized
ElectricCar initialized
```

- `super().__init__` ensures the MRO is respected, and constructors are called in the correct order.
- Each class's constructor processes the arguments it needs and forwards the rest.

---

### **3. What Is MRO (Method Resolution Order)?**

MRO determines the order in which Python searches for methods or constructors in a class hierarchy during inheritance. It ensures:

- **Left-to-right precedence** in the inheritance list.
- **Parent classes are initialized before child classes.**
- **No class is initialized multiple times.**

You can view a class's MRO using:

```python
print(ElectricCar.mro())
```

#### **MRO for `ElectricCar`**

```python
[ElectricCar, Car, Battery, object]
```

This means:

1. `ElectricCar.__init__` is called.
2. Then `Car.__init__`.
3. Followed by `Battery.__init__`.
4. Finally, `object.__init__`.

---

### **4. Does the Order of Parent Classes in Inheritance Matter?**

Yes, the order of parent classes in the inheritance list affects the MRO, which determines:

1. **Which parent class constructor is called first.**
2. **Which method is chosen if multiple parent classes define the same method.**

#### **Code Example: Different Parent Order**

```python
class Car:
    def fuel_type(self):
        return "Petrol or Diesel"

class Battery:
    def fuel_type(self):
        return "Electric Charge"

class ElectricCar(Car, Battery):
    pass

class AnotherElectricCar(Battery, Car):
    pass

ec1 = ElectricCar()
print(ec1.fuel_type())  # Resolves to Car's method

ec2 = AnotherElectricCar()
print(ec2.fuel_type())  # Resolves to Battery's method
```

#### **Output**

```
Petrol or Diesel
Electric Charge
```

#### **Explanation**

- MRO for `ElectricCar`: `[ElectricCar, Car, Battery, object]` — `Car.fuel_type` is used.
- MRO for `AnotherElectricCar`: `[AnotherElectricCar, Battery, Car, object]` — `Battery.fuel_type` is used.

---

### **5. Handling Constructors in Multiple Inheritance**

Using `*args` and `**kwargs` with `super()` allows constructors to dynamically forward arguments to the next class in the MRO. This avoids hardcoding argument passing.

#### **Code Example: Flexible Argument Handling**

```python
class Car:
    def __init__(self, brand, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = brand
        print("Car initialized")

class Battery:
    def __init__(self, capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = capacity
        print("Battery initialized")

class Engine:
    def __init__(self, horsepower, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.horsepower = horsepower
        print("Engine initialized")

class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, capacity, horsepower):
        super().__init__(brand, capacity, horsepower)
        print("ElectricCar initialized")

ec = ElectricCar("Tesla", "85kWH", "300HP")
```

#### **Output**

```
Engine initialized
Battery initialized
Car initialized
ElectricCar initialized
```

#### **Why This Works**

- `super().__init__` dynamically resolves and forwards arguments based on the MRO:
  - `[ElectricCar, Car, Battery, Engine, object]`.

---

### **Key Insights**

1. **Order Matters**:

   - The order of parent classes in the inheritance list affects the MRO and which methods or constructors are called.

2. **Use `super()`**:

   - Dynamically handles method and constructor resolution in multiple inheritance.
   - Avoids redundant or manual initialization of parent classes.

3. **MRO Determines Execution**:

   - Use `.mro()` to debug and understand the class hierarchy.

4. **Flexible Arguments**:
   - Use `*args` and `**kwargs` to allow parent classes to handle only the arguments they need, forwarding the rest.

---

### **Best Practices**

1. **Design Intelligently**:

   - Avoid unnecessarily deep or complex multiple inheritance hierarchies.
   - Use `super()` instead of directly calling parent class methods for cleaner, maintainable code.

2. **Debug with `.mro()`**:

   - Check the MRO to ensure the desired order of method resolution.

3. **Avoid Conflicts**:

   - Ensure parent classes have distinct responsibilities to prevent conflicting methods.

4. **Explicit Argument Handling**:
   - Use `*args` and `**kwargs` for flexible constructors, especially in diamond-shaped hierarchies.

---

### **Key Takeaways**

- **MRO controls method and constructor resolution.**
- **Order of inheritance matters** for resolving conflicts and determining priorities.
- **`super()` ensures clean and efficient initialization** of parent classes.
- Use **`*args` and `**kwargs` for dynamic argument handling\*\* in multiple inheritance scenarios.

This approach ensures clarity, maintainability, and avoids pitfalls in complex class hierarchies.
