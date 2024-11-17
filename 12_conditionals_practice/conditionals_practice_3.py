score = int(input("Please enter your score(maximum: 100 and minimum: 0): "))

if score >= 90 and score <= 100:
    grade = "A"
    print(grade)
elif score >= 80 and score <= 89:
    grade = "B"
    print(grade)
elif score >= 70 and score <= 79:
    grade = "C"
    print(grade)
elif score >= 60 and score <= 69:
    grade = "D"
    print(grade)
elif score < 60 and score >= 0:
    grade = "F"
    print(grade)
else:
    print("Invalid score, please input valid score value.")
    exit()
