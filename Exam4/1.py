#write a funcation to which we pass a parmeter and print the factors of a given no numbur
#for eg: factors of 12: 1,2,3,4,6,12
def factors(num):
    x = int(input("Enter a valu"))
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=",")
    print()