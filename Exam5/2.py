n = int(input("Enter number of coins: "))
coins = list(map(int, input("Enter coin numbers: ").split()))

result = 0
for coin in coins:
    result ^= coin   # XOR cancels out even numbers, leaves odd one

print("Missing coin number:", result)
