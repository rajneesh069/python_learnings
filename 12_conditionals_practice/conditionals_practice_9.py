year = int(input("Please enter the year: "))

if year < 0:
    print("Please input a valid year.")
    exit()

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year.")
else:
    print("NOT a leap year.")
