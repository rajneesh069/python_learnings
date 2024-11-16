# tuples are immutable and lists are immutable
tea_types = ("Black Tea", "Green Tea", "Oolong Tea")
print(tea_types)

# works like lists only
print(tea_types[0])
print(tea_types[-1])
print(tea_types[0:2])

# length of tuples
print(len(tea_types))  # 3

# tea_types[0] = "Masala Chai"  # not allowed as tuples are immutable

more_tea = ("Herbal Tea", "Earl Grey Tea")
all_tea = more_tea + tea_types

# conditionals in tuples
if "green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal Tea", "Herbal Tea", "Herbal Tea", "Earl Grey")
print(more_tea.count("Herbal Tea"))  # 3
print(more_tea.count("Herb"))  # 0

# unwrapping a tuple, number of value count should be same
(black, green, Oolong) = (
    tea_types  # makes 3 variables and assigns them to the values in tea_types, like JS ES6 spread operator
)
print(black)

# type of an object
type(tea_types)  # <class 'tuple'>
