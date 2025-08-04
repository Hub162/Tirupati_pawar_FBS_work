def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [10, 20, 4, 45, 99]
sorted_nums = bubble_sort(nums.copy())
second_largest = sorted_nums[-2]
print("Second largest number:", second_largest)
