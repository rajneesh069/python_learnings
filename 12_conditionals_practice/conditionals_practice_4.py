fruit = input("Please enter the name of the fruit: ").lower()
color = input("Please enter the color of the fruit: ").lower()

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Invalid color, please input valid color name.")
else:
    print("We don't have information for this fruit :(")
