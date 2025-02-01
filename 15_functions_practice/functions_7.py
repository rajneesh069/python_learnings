# we can write anything instead *args like *hello to handle variable number of parameters, but we write *args as it is a good practice


def sum_all(*args):
    # this args is a tuple which is iterable obviously
    sum = 0
    for i in args:
        i *= 2
        sum += i
    return sum


print(sum_all(5, 5, 4))
