for i in range(10):
    row = list(range(i*10+1, (i+1)*10+1))
    if i % 2 != 0:
        row.reverse()
    print(row)
