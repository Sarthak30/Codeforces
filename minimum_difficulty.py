n = int(raw_input())
a = map(int,raw_input().split())
b = []
d = []
if(n==3):
	print abs(a[0]-a[2])
else:
	for i in range(1,n-1):
		b = a[:i]+a[i+1:]
		c = [x - b[i - 1] for i, x in enumerate(b)][1:]
		d.append(max(c))
	print min(d)
