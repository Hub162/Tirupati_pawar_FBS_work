num = int(input("Enter a 3 digit num: "))

a = num % 10
num = num // 10 
b = num %10
c = num // 10
print(a,b,c)
print(a,"third digit")
print(b,"second digit")
print(c,"first digit")

