a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
