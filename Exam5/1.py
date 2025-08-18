D = [ 500, 200, 100, 50, 20, 10, 5]
amount = int(input("Enter the amount: "))

notes_count = {}
for note in D:
    if amount >= note:
        count = amount // note
        notes_count[note] = count
        amount = amount % note

print("Minimum notes required:")
for k, v in notes_count.items():
    print(f"{k}: {v}")
