n,m = map(int,raw_input().split())
a = str(raw_input())
a = list(a)
i=0
c = []
for j in range(m):
	i=0
	c = []
	while(i<(len(a)-1)):
		if not(a[i]==a[i+1]):
			if(a[i] == 'B' and a[i+1] == 'G'):
				c.append(i)
				i=i+2
			else:
			    i = i+1
			if(i>(len(a)-1)):
				break
		else:
			i=i+1
	for i in c:
		a[i],a[i+1] = a[i+1],a[i]
a = ''.join(a)
print a
		
