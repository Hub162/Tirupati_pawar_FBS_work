a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

ans = (b*b) - (4*a*c)
ans = ans ** 0.5
root1 = (-b+ ans)/ (2*a)
root2 = (-b- ans)/ (2*a)
pritn("root1: ",root1)
pritn("root2: ",root2)