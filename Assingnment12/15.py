str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Custom function to compare strings without using built-in comparison
def larger_string(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] > s2[i]:
            return s1
        elif s1[i] < s2[i]:
            return s2
        i += 1
    # If one is a prefix of the other, return the longer
    if len(s1) > len(s2):
        return s1
    else:
        return s2

result = larger_string(str1, str2)
print("Larger string is:", result)
