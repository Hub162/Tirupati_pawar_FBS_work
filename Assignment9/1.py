def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_of_factorials(n):
    if n == 1:
        return 1
    return factorial(n) + sum_of_factorials(n - 1)

n = int(input("Enter value of n: "))
print("Sum of series:", sum_of_factorials(n))
