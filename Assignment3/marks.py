marks = []
for i in range(5):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

avg = sum(marks) / 5

if avg >= 60:
    print("First Class")
elif avg >= 50:
    print("Second Class")
elif avg >= 35:
    print("Pass Class")
else:
    print("Fail")
