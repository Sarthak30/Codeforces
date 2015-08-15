n, m = map(int,raw_input().split())
a = [0]*n
for i in range(m):
	b = map(int,raw_input().split())
	c = b.index(max(b))
	a[c] = a[c]+1
print a.index(max(a))+1
	
