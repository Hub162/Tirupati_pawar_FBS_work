s = input("Enter a string: ")
n = int(input("Enter index to remove: "))
if 0 <= n < len(s):
    new_str = s[:n] + s[n+1:]
    print("Modified string:", new_str)
else:
    print("Invalid index.")
