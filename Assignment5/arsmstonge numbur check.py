num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
power = len(digits)
if sum(d ** power for d in digits) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
