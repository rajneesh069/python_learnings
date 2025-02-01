# Computing the factorial of a number using a while loop
num = 10
n = num
factorial = 1
while num > 0:
    factorial *= num
    num -= 1

print("The factorial of {} is: {}".format(n, factorial))

# using precomputation and hashing
# factorial = [0, 1]
# for i in range(2, n + 1):
#     factorial.append(i * factorial[i - 1])

# print(factorial[n])
