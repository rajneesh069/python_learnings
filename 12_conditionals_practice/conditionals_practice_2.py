age = int(input("Please enter your age: "))
day = input("What is the day today? ")

# ticket_price = 0

# if age < 18 and age > 0:
#     if day.lower() == "wednesday":
#         ticket_price = 6
#     else:
#         ticket_price = 8
# else:
#     if day.lower() == "wednesday":
#         ticket_price = 10
#     else:
#         ticket_price = 12

ticket_price = 12 if age >= 18 else 8
if day.lower() == "wed" or day.lower() == "wednesday":
    ticket_price -= 2

print("Ticket price is: ${}".format(ticket_price))
