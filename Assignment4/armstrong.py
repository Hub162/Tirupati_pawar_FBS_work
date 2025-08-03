start = int(input("Start of range: "))
end = int(input("End of range: "))
for num in range(start, end+1):
    order = len(str(num))
    sum_pow = sum(int(digit)**order for digit in str(num))
    if sum_pow == num:
        print(num)
