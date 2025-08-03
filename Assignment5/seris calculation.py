import math
n = int(input("Enter n: "))
print("Sum of factorials:", sum(math.factorial(i) for i in range(1, n + 1)))
