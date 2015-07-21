n, m = map(int,raw_input().split())
a = map(int,raw_input().split())
c = []
for i in range(n):
	c.append(i)
i = 0
while(len(a)>1):
	a[i] = a[i] - m
	if(a[i]<=0):
		a.pop(i)
		c.pop(i)
	else:
		b = a.pop(i)
		d = c.pop(i)
		a.append(b)
		c.append(d)
print c[0]+1
