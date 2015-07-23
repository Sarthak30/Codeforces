n,m = map(int,raw_input().split())
out = [-1]*n
bulbs = map(int,raw_input().split())
for i in bulbs:
    j=i-1
    while j < n and out[j] == -1:
        out[j]=str(i)
        j+=1
print(' '.join(out))
