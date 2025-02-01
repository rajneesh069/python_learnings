# lists are mutable
names = ["Rajneesh", "Sachin", "Kartikey", "Vivek"]
print(names)

print(names[0])  # prints the 0th element
print(names[-1])  # prints the last element, negative indices are allowed
print(names[:2])  # prints upto 1, and excludes 2
print(names[0::2])

names[1] = "Mukul"

names[1:2] = "Lulin"
print(names)  # ['Rajneesh', 'L', 'u', 'l', 'i', 'n', 'Kartikey', 'Vivek']
# in the above case "Lulin" was treated as array instead of a string

names = ["Rajneesh", "Sachin", "Kartikey", "Vivek"]
names[1:2] = ["Lulin"]  # now it will work as expected
print(names)  # at position 1 "Sachin" got replaced with "Lulin"

names[1:3] = [
    "Sachin",
    "Lulin",
]  # from places 1 to 2(both inclusive) the elements will be replaced as intended
print(names)

print(names[1:1])  # prints empty []

names[1:1] = [
    "Test Name 1",
    "Test Name 2",
]  # shifts the values at position 1 and inserts these 2 names

print(names)

names[1:3] = []  # inserts nothing, i.e, deletes the elements from that range
print(names)

# iterating through the list
for name in names:
    print(
        name, end="-"
    )  # instead of a new line character it inserts a "-" in between elements

print()

# conditionals in lists
if "Rajneesh" in names:
    print("True")

# appending in the list
names.append("Munni")
if "Munni" in names:
    print("Munni is present.")

# popping off the last item from the list
removed = names.pop()  # returns the removed element
print(removed)

# to remove something in the list
names.remove("Lulin")  # returns nothing

# inserting in a list
names.insert(1, "Lulin")  # inserts "Lulin" at index = 1
print(names)

names_copy = names.copy()  # both have different references now

names_copy.append("Munni")

print(names_copy, names)  # both will have different elements obviously

# list comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)  # in range(0, 10), obviously 10 is exclusive
# the above code prints a list of squared numbers upto 9

cubed_numbers = [x**3 for x in range(10)]
print(cubed_numbers)
# the above code prints a list of cubed numbers upto 9
