user = {
    "first_name": "Rajneesh",
    "last_name": "Mishra",
    "email": "rajneesh.mishra9616@gmail.com",
}

# accessing the elements
print(user["first_name"])  # Rajneesh

print(user.get("first_name"))

print(user.get("non_existing_key"))  # returns nothing(None) if the key doesn't exist
# print(user["non_existing_key"])  # gives error

# changing the value of key
user["email"] = "rajneesh.mishra9616@outlook.com"
print(user)

# iterating over keys in a dictionary
for key in user:
    print(
        key, ":", user[key]
    )  # it prints key actually and NOT values, to get values we can simply put user[key]

# get the dictionary item and print its key and value
for key, value in user.items():
    print(key, value)

# conditionals in dictionary, applies on keys only
if "first_name" in user:
    print("First Name of the user is available")

# length of dictionary = number of keys
print(len(user))  # 3

# adding a new key in a dictionary
user["address"] = "Gonda, Uttar Pradesh, 271001"
print(user)
print(len(user))  # 4

# pop a key/value pair from the dictionary
user.pop("address")  # takes a key as an input

print(
    user
)  # prints the user dictionary without the "address" key because it was popped off

print(len(user))  # 3

user.popitem()  # pops off the last item
print(user)
print(len(user))  # 2

# deleting the reference from memory itself
del user["last_name"]
print(user)
print(len(user))  # 1

user_copy = user.copy()  # different references

# nesting of dictionary is allowed
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "tea": {"Green": "Mild", "Black": "Strong"},
}

print(tea_shop)
print(tea_shop["chai"]["Masala"])  # to access deeply nested keys

# dictionary comprehension just like lists
squared_nums = {x: x**2 for x in range(10)}
print(squared_nums)

squared_nums.clear()  # clears the dictionary


keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

new_dict = dict.fromkeys(keys, keys)  # puts the whole array as a value
print(new_dict)
