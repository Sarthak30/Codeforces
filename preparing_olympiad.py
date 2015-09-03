from itertools import combinations
L = lambda: map(int,raw_input().split())
n, l, r, x = L()
c,ans = L(),0

for size in xrange(2,len(c)+1):
    for s in list(combinations(c,size)):
        if l <= sum(s) <= r and max(s) - min(s) >= x:
            ans += 1

print ans
