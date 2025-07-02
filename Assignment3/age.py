total = 0
for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    ticket = float(input("Enter ticket price: "))
    
    if age < 12:
        total += ticket * 0.7  # 30% discount
    elif age > 59:
        total += ticket * 0.5  # 50% discount
    else:
        total += ticket

print("Total amount to pay for 5 people:", total)
