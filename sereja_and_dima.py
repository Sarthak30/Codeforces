n = int(raw_input())
c = map(int,raw_input().split())
s = 0
d = 0
k = 0
while not(len(c)==0):
	j = len(c)-1
	if(k==0):
		if(c[0]>c[j]):
			s = s + c[0]
			c.pop(0)
		else:
			s = s + c[j]
			c.pop(j)
		k = 1
	elif(k==1):
		if(c[0]>c[j]):
			d = d + c[0]
			c.pop(0)
		else:
			d = d + c[j]
			c.pop(j)
		k = 0
print s,
print d
