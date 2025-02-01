# This is how loops work internally in python, based on iterables, iterators and next() method.
my_list = [1, 2, 3]

I = iter(
    my_list
)  # returns an object(stateful) which knows how to traverse the iterable object


print(I.__next__())  # gives the current value and moves onto the next value
print(I.__next__())  # gives the current value and moves onto the next value
print(I.__next__())  # gives the current value and moves onto the next value
print(
    I.__next__()
)  # Raises StopIteration exception when reaches at the last index of the list

print(
    I is my_list
)  # false, my_list contains the reference to the first element of the list while I is the iterator for the iterable object
# For files, the iterator is same as the reference to the first element.
f = open("file.py")
print(iter(f) is f)  # True
f.__next__()  # prints the first line
f.__next__()  # prints the second line
f.__next__()  # StopIteration exception is raised as it reached at the end of the list

# Range is also an iterable
R = range(0, 5)
Iter = iter(R)
print(next(Iter))  # prints 0
print(next(Iter))  # prints 1
print(next(Iter))  # prints 2
print(next(Iter))  # prints 3
print(next(Iter))  # prints 4
print(next(Iter))  # Raises StopIteration Exception
