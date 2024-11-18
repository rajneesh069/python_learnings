username = "Rajneesh"


def function():
    username = "Sachin"
    print(username)  # prints Sachin


print(username)  # prints Rajneesh


def function2():
    print(username)  # prints Rajneesh


x = 99


def function3(y):
    z = x + y
    return z


result = function3(1)
print(
    result
)  # prints 100, x from the global scope and y from the function scope given in parameters


def function4():
    x = 88
    print(x)  # prints 88


# def function5():
#     global x  # shouldn't be done, a bad practice
#     x = 132


# function5()
# print(x)  # value changed to 132


def f1():
    x = 88

    def f2():
        print(x)

    f2()


f1()  # prints 88, because it searches for x in the nearest lexical scope and then goes up if it doesn't find it nearby


def f3():
    x = 88

    def f4():
        print(x)

    return f4


my_result = f3()  # f3 returns the reference of f4, hence my_result is f4

my_result()  # prints 88, like JS, it has closure, i.e., along with the function, it's lexical scope is also returned


def chai(num):
    def actual(x):
        return x**num

    return actual


# closures are also known as factory functions in python.

f = chai(2)  # returns us the actual function's closure
g = f(3)  # we got the value returned by 'actual' function inside the 'chai' function

print(f)  # the reference of 'actual' function and it's closure
print(g)  # we got 9, i.e., 3**2

print(
    chai(2)(3)
)  # can also be called like this, function currying in JS has the same concept
