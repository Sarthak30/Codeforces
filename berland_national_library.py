n = int(raw_input())
c = []
d = 0
while(n):
	n = n-1
	a,b = raw_input().split()
	if(a=='-'):
		if(b in c):
			c.remove(b)
		else:
			d = d+1
	else:
		c.append(b)
	d = max(d,len(c))
print d
