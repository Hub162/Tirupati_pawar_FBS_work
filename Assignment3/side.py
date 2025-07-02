a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")
