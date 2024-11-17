s = input("Please input a string: ")
l = list(s)
start = 0
end = len(l) - 1

while start < end:
    temp = l[end]
    l[end] = l[start]
    l[start] = temp
    start += 1
    end -= 1

print("The reversed string is:", "".join(l))

# Another way
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string

print("The reversed string is:", reversed_string)
