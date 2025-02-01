n = 10
even_sum = 0

for i in range(0, n + 1):
    if i % 2 == 0:
        even_sum += 1
print("Number of even numbers from 0 to {}(inclusive) is: {}".format(n, even_sum))
