a = int(input("Enter angle A: "))
b = int(input("Enter angle B: "))
c = int(input("Enter angle C: "))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Valid triangle")
else:
    print("Invalid triangle")
