feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))
total_inches = feet * 12 + inches
centimeters = total_inches * 2.54
meters = int(centimeters // 100)
remaining_cm = centimeters % 100
print(f"{feet} feet and {inches} inches = {meters} meter(s) and {remaining_cm:.2f} centimeter(s)")
