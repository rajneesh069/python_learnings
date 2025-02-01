weather = input("How's the weather today? ").lower()

if weather == "sunny":
    print("Go for a walk.")
elif weather == "rainy":
    print("Read a book.")
elif weather == "winter":
    print("Brew some coffee/tea and enjoy near the fireplace.")
elif weather == "snowy" or weather == "snow":
    print("Build a snowman!")
else:
    print("Do whatever you want!!")
