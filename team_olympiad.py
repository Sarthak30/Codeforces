a = int(raw_input())
b = map(int,raw_input().split())
b1i = []
b2i = []
b3i = []
for i in range(0,a):
	if b[i]==1:
		b1i.append(i)
	elif b[i]==2:
		b2i.append(i)
	else:
		b3i.append(i)
x = min(len(b1i),len(b2i),len(b3i))
print x
for i in range(0,x):
	print str(b1i[i]+1)+" "+str(b2i[i]+1)+" "+str(b3i[i]+1)
