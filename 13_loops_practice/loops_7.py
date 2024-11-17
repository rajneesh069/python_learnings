while True:
    number = int(input("Please enter a number between 1 and 10(both inclusive): "))
    if 0 < number < 11:
        print("Thanks!")
        break
    else:
        print("Invalid Number, try again!!")
