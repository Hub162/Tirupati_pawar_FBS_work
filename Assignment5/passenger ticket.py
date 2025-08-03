num_passengers = int(input("Enter number of passengers: "))
ticket_price = float(input("Enter price per ticket: "))

total_cost = 0

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i + 1}: "))
    if age < 12:
        cost = ticket_price * 0.7
    elif age > 59:
        cost = ticket_price * 0.5
    else:
        cost = ticket_price
    total_cost += cost

print(f"\nTotal cost for all passengers: {total_cost:.2f}")
