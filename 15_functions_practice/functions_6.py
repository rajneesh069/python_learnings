def add(x, y):
    return x + y


result = add(2, 3)  # for reusability it is a great way to define functions

# but when we have to use a function once or twice then we directly use lamda functions

cube = (
    lambda x: x**3
)  # lambda function which takes x as a parameter and returns the cube of it


another_cube = cube(
    3
)  # so another_cube variable has a fixed value which is 27 in this case and NOT the function definition itself!

print(another_cube)

another_cube = cube  # this is a reference and now it can be called with dynamic values
print(another_cube(4))  # prints 64
