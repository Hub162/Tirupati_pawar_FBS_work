num = int(input("Enter a three-digit number: "))
if 100 <= num <= 999:
    sum_digits = sum(int(d) for d in str(num))
    print(f"Sum of digits: {sum_digits}")
else:
    print("Please enter a valid three-digit number.")