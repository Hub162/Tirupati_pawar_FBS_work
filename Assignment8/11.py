def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

num = int(input("Enter a number: "))
if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
