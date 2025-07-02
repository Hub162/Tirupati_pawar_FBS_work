cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
if sp > cp:
    print("Profit of", sp - cp)
elif cp > sp:
    print("Loss of", cp - sp)
else:
    print("No profit, no loss")
