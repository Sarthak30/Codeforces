from collections import Counter
n = input()
arr = [ raw_input() for i in xrange(n) ]
a = Counter()
b = []
for i in xrange(n):
  nm, s = arr[i].split()
  a[nm] += int(s)
  b.append((nm, a[nm]))
mx = max(a.values())
print [nm for (nm, s) in b if s >= mx and a[nm] == mx][0]
