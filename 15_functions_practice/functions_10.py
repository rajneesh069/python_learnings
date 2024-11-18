# recursive functions


def factorial(x):
    if x == 1 or x == 0:
        return 1
    return factorial(x - 1) * x


result = factorial(5)
print(result)
print(factorial(6))
