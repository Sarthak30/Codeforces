n = input()
ls = [0]*n
for i in range(n):
    ls[i] = int(raw_input())
    if ls[i]!=-1:
        ls [i] -= 1
ans = 1
for i in range(n):
    j=i
    cnt=1
    while ls[j]!=-1:
        cnt += 1
        j = ls[j]
    ans = max(ans,cnt)
print ans
