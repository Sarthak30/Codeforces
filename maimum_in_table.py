def elem(row, col):
    if row == 1 or col == 1:
        return 1
    return elem(row - 1, col) + elem(row, col - 1)
    
a = int(raw_input())
print elem(a,a)
