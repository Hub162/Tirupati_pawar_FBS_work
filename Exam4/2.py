#write a progarm to find factorial of all no in givan range recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_in_range(start, end):
    for i in range(start, end + 1):
        print(f"Factorial of {i} is {factorial(i)}")

start_num = 1
end_num = 5
factorial_in_range(start_num, end_num)
