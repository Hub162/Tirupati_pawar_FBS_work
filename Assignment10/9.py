n = int(input("How many numbers? "))
nums = []
for _ in range(n):
    nums.append(int(input("Enter number: ")))

even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]

print("Even list:", even)
print("Odd list:", odd)
