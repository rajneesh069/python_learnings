password = input("Please enter your password to check its strength: ").strip()

if len(password) < 6:
    print("Weak. Please increase the number of characters.")
elif len(password) >= 6 and len(password) <= 10:
    print("Medium.")
else:
    print("Strong.")
