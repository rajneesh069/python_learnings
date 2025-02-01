s = "teeter"

# Brute Force way: O(N^2) time complexity, O(1) space complexity
# for char in s:
#     if s.count(char) == 1:
#         print("First non-repeating character is:", char)
#         break

# Optimized Way: O(N) space complexity and O(N) time complexity
frequency_of_characters_in_s = {}

# for char in s:
#     if frequency_of_characters_in_s.get(char) == None:
#         frequency_of_characters_in_s[char] = 1
#     else:
#         frequency_of_characters_in_s[char] += 1

for char in s:
    frequency_of_characters_in_s[char] = frequency_of_characters_in_s.get(char, 0) + 1


for item in frequency_of_characters_in_s.items():
    if item[1] == 1:
        print(item[0])
        break
