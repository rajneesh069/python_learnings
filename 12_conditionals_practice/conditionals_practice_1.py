# Age categorization
age = int(input("Please enter the age: "))

if age < 13 and age > 0:
    print("Children")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age > 19 and age <= 59:
    print("Adult")
elif age > 59:
    print("Senior")
else:
    print("Invalid Age!")
