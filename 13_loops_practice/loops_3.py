n = int(input("Please enter the number: "))

for i in range(1, 11):
    if i == 5:
        # print("5th iteration skipped.")
        continue
    print(n, "X", i, "=", i * n, end="\n")
