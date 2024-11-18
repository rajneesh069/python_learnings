# Generator function with yield


# first we discuss the normal function
def even_generator(num):
    for i in range(0, num + 1, 2):  # the last argument is step
        print(i)
        return i


# We can return a list but we want numbers and not a list!!!

# for even_nums in even_generator(5):
#     print(even_nums)

# The above line gives error because 'int' is not an iterable.

# print(even_generator(5))  # prints 0 and exits!

# So now at the first iteration only, we'll be returned 0 and the function will terminate, but what if we wanted to generate a new value each time the function was called and what if we wanted the function to be independent for different loops too like when they are iterated through different loops?


def even_gen(num):
    for i in range(0, num + 1, 2):
        yield i


for even_numbers in even_gen(5):
    print(even_numbers)

# the above loop prints all the even numbers till 5.

for even_nums_2 in even_gen(5):
    print(even_nums_2)


gen_obj1 = even_gen(
    5
)  # generators return a generator object which implements iter() and next() function both
gen_obj2 = even_gen(5)

print(next(gen_obj1))  # 0
print(next(gen_obj2))  # 0
print(next(gen_obj2))  # 2
print(next(gen_obj2))  # 4
print(next(gen_obj1))  # 2
