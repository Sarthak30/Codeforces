n, k = map(int, raw_input().split())
c = map(int, raw_input().split())
c.sort()
s = 0
for i in range(len(c)-1,-1,-k):
	s = s + (c[i]-1)
print 2*s
