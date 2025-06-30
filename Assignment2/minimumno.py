amount = int(input("Enter amount: "))
notes = [100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes needed:")
for note in notes:
    count = amount // note
    if count:
        print(f"{note} x {count}")
    amount %= note