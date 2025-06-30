P = float(input("Enter Principal: "))
T = float(input("Enter Time (years): "))
R = float(input("Enter Rate of Interest: "))
CI = P * ((1 + R / 100) ** T) - P
print(f"Compound Interest: {CI:.2f}")