start = int(input("Start of range: "))
end = int(input("End of range: "))
divisor = int(input("Enter divisor: "))
for i in range(start, end+1):
    if i % divisor == 0:
        print(i)
