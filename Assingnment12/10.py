s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
len1 = len2 = 0
for _ in s1:
    len1 += 1
for _ in s2:
    len2 += 1
if len1 > len2:
    print("Larger string is:", s1)
else:
    print("Larger string is:", s2)
