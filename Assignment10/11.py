nums = [10, 15, 20, 30, 40, 45, 60]
m = int(input("Enter first divisor (m): "))
n = int(input("Enter second divisor (n): "))

result = [x for x in nums if x % m == 0 and x % n == 0]
print(f"Numbers divisible by both {m} and {n}:", result)
