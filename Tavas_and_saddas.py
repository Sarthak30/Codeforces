n = raw_input()
ans = 1
for x in n:
    ans = 2 * ans + (1 if x == '7' else 0)
print ans - 1
