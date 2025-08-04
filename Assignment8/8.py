def reverse_number(n):
    return int(str(n)[::-1])

num = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(num))
