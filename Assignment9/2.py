def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def armstrong_sum(num, digits):
    if num == 0:
        return 0
    return power(num % 10, digits) + armstrong_sum(num // 10, digits)

num = int(input("Enter a number: "))
digits = len(str(num))
if num == armstrong_sum(num, digits):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
