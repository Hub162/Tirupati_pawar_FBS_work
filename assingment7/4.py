n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(i + j - 1) for j in range(i)))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + " ".join(str(n - i + j + 1) for j in range(i)))
