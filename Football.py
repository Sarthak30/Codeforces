n = int(raw_input())
d = {}
c = []
while(n>0):
	a = raw_input()
	if(a in d):
		d[a] = d[a]+1
	else:
		d[a] = 1
		c.append(a)
	n = n-1
if(len(c) == 1):
	print c[0]
elif(d[c[0]] < d[c[1]]):
	print c[1]
else:
	print c[0]
