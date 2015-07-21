n, k = map(int,raw_input().split())
a = map(int,raw_input().split())
b = sorted(a)
c = []
s = 0
for i in b:
	s = s+i
	c.append(i)
	if(s==k):
		break 
	if(s>k):
		c.pop(-1)
if(len(c)==-1):
	print "-1"
else:
	d = []
	for i in c:
		for j in range(n):
			if i==a[j] and j not in d :
				d.append(j)
				break 
	print len(d)
	for i in d:
		print str(i+1),
