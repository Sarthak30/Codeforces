a = int(raw_input())
c = map(int,raw_input().split())
d = []
e = []
for i in c:
	if(i%2==0):
		e.append(i)
	else:
		d.append(i)
if(len(e)==1):
	print (c.index(e[0])+1)
else:
	print (c.index(d[0])+1)
