n, m, a, b = map(int,raw_input().split())
c = n/m
if(n%m is not 0):
	c=c+1
d = a*n
e = c*b
if(d<e):
	print d
else:
	print e
