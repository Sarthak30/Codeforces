n, c = map(int,raw_input().split())
x = map(int,raw_input().split())
d = []
for i in range(n-1):
	d.append(x[i]-x[i+1])
a = d.index(max(d))
z = x[a]-x[a+1]-c
if(z<0):
	print "0"
else:
	print z
