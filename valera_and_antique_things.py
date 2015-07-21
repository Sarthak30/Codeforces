n, v = map(int,raw_input().split())
j = 0
d = []
for i in range(n):
	j = j + 1
	c = map(int,raw_input().split())
	c.pop(0)
	for k in c:
		if(k<v):
			d.append(j)
			break
print len(d)
if not(len(d)==0):
	for i in d:
		print i,
