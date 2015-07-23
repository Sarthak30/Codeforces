k = int(raw_input())
a = map(int,raw_input().split())
p = []
n = []
z = []
flag = 0
for i in a:
	if(i<0 and len(n) < 1):
		n.append(i)
	elif(i>0 and len(p) < 1):
		p.append(i)
		flag = 1
	else:
		z.append(i)
i = 0
if flag == 0:
	while i<len(z):
		if(z[i] != 0 and len(p)<2):
			p.append(z[i])
			z.pop(i)
		else:
			i=i+1
print len(n), 
for i in n:
	print i,
print 
print len(p),
for i in p:
	print i,
print 
print len(z),
for i in z:
	print i,
