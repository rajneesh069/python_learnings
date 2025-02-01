# the data type of a variable is in the memory and NOT in the language itself.
# numbers and strings are treated differently as compared to other data types. They are not Garbage collected instantly once their reference goes out of scope, rather 'python' collects them a bit later, i.e, caches the reference for small integers and strings depending on it's usage patterns.
# even if we assign the same data to mutable objects they get different references

h1 = [1, 2, 3]
h2 = h1[:]  # this copies the list h1 and then creates a new reference
print(h1)  # [1,2,3]
print(h2)  # [1,2,3]

h1[0] = 23
print(h2)  # [1,2,3]
print(h1)  # [23, 2, 3]

m = [1, 2, 3]
n = m
print(m == n)  # true, checks just the value
print(n is m)  # true, same memory reference
n = [1, 2, 3]
print(
    n is m
)  # false, because mutable data types hence different references are assigned
