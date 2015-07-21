n = int(raw_input())
a = map(int,raw_input().split())
d = []
b = map(str,sorted(a))
i = 0
while(b!=a and i<n):
	c = a.index(min(a[i:]))
	a[c], a[i] = a[i], a[c]
	a[i] = str(a[i])
	d.append((i,c))
	i = i+1
print i
for i in d:
	print i[0],i[1]
