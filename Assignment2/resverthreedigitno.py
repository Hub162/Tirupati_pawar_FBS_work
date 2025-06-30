num = int(input("Enter a three-digit number: "))
if 100 <= num <= 999:
    reverse = int(str(num)[::-1])
    print(f"Reversed number: {reverse}")
else:
    print("Enter a valid three-digit number.")
