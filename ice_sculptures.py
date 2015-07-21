import sys

n = input()
a = map(int, raw_input().split())

i = 1
res = -sys.maxint
while i <= n/3:
    if (not n%i) and n/i >=3:
        for j in xrange(i):
            res = max(res, sum(a[j::i]))
    i += 1

print res
