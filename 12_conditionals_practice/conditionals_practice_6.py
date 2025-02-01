distance = int(input("Please enter the distance(in kms): "))

if distance < 3 and distance > 0:
    transport = "Walk"
elif distance >= 3 and distance <= 15:
    transport = "Bike"
elif distance > 15:
    transport = "Car"
else:
    print("Please input valid distance value.")
    exit()

print(transport)
