n,t = map(int,raw_input().split())
a = map(int,raw_input().split())
s,i,m = 0,0,0
for x in xrange(n):
    s += a[x]
    while s > t:
        s -= a[i]
        i += 1
    m = max(m,x-i+1)
print m
