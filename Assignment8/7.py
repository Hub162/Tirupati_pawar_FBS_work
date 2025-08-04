def sum_digits(n):
    return sum(int(d) for d in str(n))

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))
