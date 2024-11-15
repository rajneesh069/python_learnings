# python has a very strong eco-system for numbers.
# in python, the numbers aren't a single object rather a group of objects.
# in python, integer, float, decimals, fractions, booleans, sets(almost) are treated as numbers.
# numbers can be expanded by using other libraries.
# under the hood, the compilers are of C/C++, the level of precision of double in C is same as in python.
import math

x = 2
y = 3
z = 4

print(x + y)
# if we were to do BODMAS operations, use parentheses as without them things will be ambiguous
print(x + y * z)  # ambiguous
print((x + y) * z)  # non-ambiguous
print(x + (y * z))  # non- ambiguous

a = 40
b = 2.23
# c = a+b
# Try to keep the data types same, instead of different, like this:
c = float(a) + b
# or
c = a + int(b)
# the above 2 cases are more preffered as it clarifies what will be the output.

# Some operators have been overloaded too
s1 = "Rajneesh"
s2 = "Mishra"
s3 = s1 + s2  # "RajneeshMishra"

print(x, y, z)  # gives out a tuple as a result, i.e., (1,2,3)
print(x + 1, y * 2)  # (2, 4)

print(y % 2)  # modulo operator, gives out the remainder after the division, prints 0

print(
    2**100
)  # raises 2 to the power of 100, and it will show all values, that's how much powerful numbers are in python

print(2**1000)  # raises 2 to the power of 1000, this one too, gets totally printed


result = 1 / 3.0  # correct way is 1.0/3.0, but let it be for now
print(result)  # 0.3333333


## Comparison in Python
print(1 < 2)  # True
print(1 > 2)  # False
# True and False are treated as numbers(1 and 0 respectively) only.

print(
    x < y < z
)  # It's confusing and not a good way to write, although we'll get True for this


print(
    x < y and y < z
)  # Good practice, the above one is same as this but this is more expressive

print(1 == 2 < 3)  # False, not a good way to write
print(1 == 2 and 2 < 3)  # False, but a good way to write

math.floor(
    3.5
)  # gives the value towards -ve infinity/gives us the nearest most bottom integer, prints 3
math.floor(-3.5)  # prints -4

math.trunc(2.8)  # takes us towards 0, prints 2
math.trunc(-2.8)  # prints -2

# The precision in python is almost infinite

# Complex numbers
print((2 + 1j) * 3)

# Octal numbers
print(0o20)

# Hexadecimal numbers
print(0xFF)

# Binary Numbers
print(0b1000)

# We have functions for these by the way
print(oct(10))  # prints the octal value for decimal based number 10
print(bin(8))  # prints the binary value for decimal based number 10
print(hex(13))  # prints the hexadecimal value for decimal based number 10

# bitwise operations
x = 1
print(x << 2)  # right shift x by 2 places
print(x | 2)  # do bitwise or with 2

import random

print(random.random())  # prints a random decimal value
print(random.randint(1, 10))  # prints a random integer between 1 to 10


l1 = ["rajneesh", "mukul", "monu", "kritansh", "mayank", "vrushik"]
print(random.choice(l1))  # prints a random value from the list
(random.shuffle(l1))  # shuffles the list randomly
print(l1)  # prints the shuffled list

print(0.1 + 0.1 + 0.1 - 0.3)  # decimal precision causes error hence 0 is not printed
# use Decimal function from decimal library for proper results and whenever precision in decimal numbers comes into play
from decimal import Decimal

print(
    Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
)  # Decimal('0.0')

from fractions import Fraction

my_fraction = Fraction(2, 3)  # 2/3

# sets in python
set1 = {1, 2, 3, 4}
print(set1 & {1, 3})  # Intersection of two sets
print(set1 | {1, 3})  # Union of 2 sets
print(set1 | {9, 1, 3})  # {1,2,3,4,9}

print(True == 1)  # True
print(False == 0)  # False

print(True is 1)  # False, in memory it's different
print(False is 0)  # False, in memory it's different

print(
    True + 3
)  # prints 4, value wise True = 1, though this shouldn't be done and counts as a bad practice
