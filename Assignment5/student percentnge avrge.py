num_students = int(input("Enter number of students: "))
all_percentages = []

for i in range(num_students):
    print(f"\nEnter marks for student {i + 1}")
    total = 0
    for j in range(5):
        mark = float(input(f"Subject {j + 1} marks: "))
        total += mark
    percentage = total / 5
    all_percentages.append(percentage)

print("\nPercentages:")
for i, p in enumerate(all_percentages, 1):
    print(f"Student {i}: {p:.2f}%")

average = sum(all_percentages) / num_students
print(f"Average Percentage: {average:.2f}%")
