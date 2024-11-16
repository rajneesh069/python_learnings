x = 10
y = x
x = 15

print(x)  # prints 15, as it points to a new memory location with 15 as a value
print(y)  # points to 10 still

# x and y are immutable integer objects.

s1 = "hello"
s1 = "world"  # s1 is now pointing to a new memory location which contains "world" as it's value, "hello" the object itself remains unchanged, that's what immutability is

s2 = s1
s1 = "something_new"

print(
    s2
)  # now s2 points to "world" while s1 points to "something_new" and "hello" was garbage collected upon execution because no reference variable was pointing to it.

# s1[0] = 'K' # gives error since it is immutable


# Mutable object: List
a = [1, 2, 3]
b = a  # `b` and `a` point to the same list
a.append(4)  # Modify the list

print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
# The object itself got changed unlike strings or integers.

k = 10
l = 10
print(
    k is l
)  # True, because for immutable data types same reference can be reused(for efficiency)

l = 100
print(
    k is l
)  # False, now a new object is created with value = 10 and l points to it now

# For mutable objects, each time a new reference is created
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # false, because different references

a = b  # we made the references same, now if we change anything in either 'a'  or 'b' changes will be reflected to both, but in immutable data types, it won't happen as a new object will be created and the value will be assigned to that reference

a[0] = 100
print(b)  # [100, 2, 3]
