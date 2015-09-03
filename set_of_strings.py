k = int(raw_input())
q = raw_input()
if(k==1):
	print "YES"
	print q
	exit()
if(k>len(q)):
	print "NO"
	exit()
c = 0
a = []
b = []
l = len(q)
j = 0
for i in range(l):
	if(q[i] not in a):
		a.append(q[i])
		b.append(q[j:i])
		if(q[j:i] == ""):
			c = c-1
		c = c+1
		j = i
	if(c==k-1):
		c = c+1
		b.append(q[i:])
		break
if(c==k):
	print "YES"
	for i in b:
		if(i==""):
			continue
		print i
else:
	print "NO"
		
