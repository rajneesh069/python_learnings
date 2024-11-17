pet = input("Please enter the species of your pet(in years): ").lower()
age = int(input("Please enter the age: "))
if age <= 0:
    print("Please enter valid age.")
    exit()

if pet == "dog":
    if age < 2:
        print("Puppy Food")
    else:
        print("Senior Dog Food")
elif pet == "cat":
    if age < 2:
        print("Kitten Food")
    elif age > 5:
        print("Senior Cat Food")
else:
    print("We don't have information about this pet :(")
