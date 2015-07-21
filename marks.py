n,m = map(int, str(raw_input()).split())
final = [0]*n
marks = [list(raw_input().strip()) for i in range(n)]
for j in range(m):
    x = [marks[i][j] for i in range(n)]
    for i in range(n):
        if marks[i][j] == max(x):
            final[i] = 1
print sum(final)
