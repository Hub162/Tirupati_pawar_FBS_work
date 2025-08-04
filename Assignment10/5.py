nums = [1, 2, 3, 4, 2, 5, 2]
x = int(input("Enter number to search: "))
if x in nums:
    print(f"{x} is present {nums.count(x)} times.")
else:
    print(f"{x} is not present in the list.")
