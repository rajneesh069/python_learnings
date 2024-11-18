# to handle multiple keyword arguments(name="Rajneesh") we use the following syntax


def print_kwargs(**kwargs):
    # the kwargs is a dictionary and can be iterated like such, just like in case of *args it was a tuple
    for key, value in kwargs.items():
        print(key, ":", value)


print_kwargs(first_name="Rajneesh", last_name="Mishra", age=22)
