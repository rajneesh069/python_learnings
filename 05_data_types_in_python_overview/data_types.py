x = 10  # `x` is an immutable integer
y = "string"  # `y` is an immutable string, strings are somewhat treated like arrays(lists)

print(len(y))  # prints the length of the string
print(y[0])  # prints 's'
print(
    y[-1]
)  # prints 'g', basically negative numbers make it start from the back of the string

print(y[1:3])  # prints 'tr', starting index is included and ending index is excluded
# y[0] = "D"  # gives error since `y` is immutable

print(dir(y))  # prints all the methods that can be applied to a data-type

my_list = [1, 2, 3, 4, 5, "chai", 3.14159]  # same as arrays

print(my_list)  # prints the list
print(len(my_list))  # prints the length of the list
print(my_list[0])  # prints 1
print(my_list[-1])  # prints 3.14159

my_dict = {"key": "value", "comics": ["Marvel", "DC"]}
print(my_dict)  # prints the dictionary
print(my_dict["key"])  # prints value
# print(my_dict["some_random_key"]) # gives error that the key doesn't exist

my_tup = (1, 2, 4)
print(my_tup[0])  # prints 1
print(len(my_tup))  # prints the length of tuple
