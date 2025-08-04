n = 4
for i in range(1, n + 1):
    left = " ".join(str(j) for j in range(1, i + 1))
    right = " ".join(str(j) for j in range(i, 0, -1))
    print(f"{left:<8}{right}")
