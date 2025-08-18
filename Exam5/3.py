Data = [[101,"Seema",45000],[340,"Rajani",13000],
        [210,"Tannu",14000],[320,"Suresh",35000]]

# Sort based on salary (3rd element)
sorted_data = sorted(Data, key=lambda x: x[2])

print("Sorted employee list by salary:")
for emp in sorted_data:
    print(emp)
