def fibonacci_series(n):
    a, b = 1, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter number of terms: "))
print("Fibonacci Series:", fibonacci_series(n))
