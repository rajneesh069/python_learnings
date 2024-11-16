# in """ """ strings, formatting remains safe.

name = "Rajneesh Mishra"

first_char = name[0]
print(first_char)

last_char = name[-1]
print(last_char)

# slicing a string
first_name = name[0:8]
print(first_name)

# slicing cases
num = "0123456789"
print(num[0:])
print(num[:-1])
print(num[-1:])

name = "    Sachin Mishra     "
print(name.strip())  # removes leading and ending whitespaces

print(name.replace("Sachin", "Rajneesh").strip())

name = "Rajneesh, Sachin, Kartikey"
print(
    name.split(",")
)  # splits and creates an array, based on what's passed in the split function

name = "Rajneesh Mishra"
print(
    name.find("Mishra")
)  # it gives the starting position of the string, if it doesn't find it, the method returns -1

name = "Rajneesh Rajneesh Rajneesh Mishra"
print(name.count("Mishra"))  # prints 3

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai."
print(
    order.format(quantity, chai_type)
)  # string formatting, using variables in strings

list = ["Rajneesh", "Vivek", "Mukul", "Kritansh", "Mayank"]
print(
    " ".join(list)
)  # makes a string out of a list, Rajneesh Vivek Mukul Kritansh Mayank
print(
    ", ".join(list)
)  # makes a string out of a list, Rajneesh, Vivek, Mukul, Kritansh, Mayank

name = "Rajneesh Mishra"
print(len(name))  # length of the string

# to iterate over the string
for letter in name:
    print(letter)

string = 'She said, "Rajneesh is awesome" '
print(string)

string = "Rajneesh\nMishra"
print(string)

path = r"c:\users\pwd"  # r means raw here
print(path)

name = "Rajneesh Mishra"
print("Rajneesh" in name)  # true
print("Rajnee" in name)  # true
print("Rajni" in name)  # false
