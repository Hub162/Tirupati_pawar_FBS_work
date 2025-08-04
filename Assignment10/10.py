nums = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Enter element to remove: "))
nums = [i for i in nums if i != x]
print("List after removing:", nums)
