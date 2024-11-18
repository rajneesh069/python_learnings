import math


def circle(r):
    return (
        math.pi * r * r,
        math.pi * 2 * r,
    )  # tuple is returned when multiple values are being returned like this, we can however explicitly return a list, tuple or anything else.


area, circumference = circle(5)

print(round(area, 3), round(circumference, 3))
