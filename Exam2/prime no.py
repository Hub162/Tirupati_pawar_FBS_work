start=int(input("Enter a start no: "))
stop=int(input("Enter a stop no"))

for x in range(start,stop):
    for i  in range(2,x):
        if(x % i == 0):
            break
    else:
        print(x)