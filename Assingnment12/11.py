string = input("Enter a string: ")
result = ''
for ch in string:
    if ch == ' ':
        result += '-'
    else:
        result += ch
print("Modified string:", result)
