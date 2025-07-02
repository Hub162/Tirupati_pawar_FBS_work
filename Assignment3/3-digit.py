num = input("Enter a 3-digit number: ")
if num == num[::-1] and len(num) == 3:
    print("Palindrome number")
else:
    print("Not a palindrome")
