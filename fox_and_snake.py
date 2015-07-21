a, b = map(int,raw_input().split())
i=0
while(i<a):
	j=0
	c=[]
	if(i%2==0):
		while(j<b):
			c.append('#')
			j=j+1
		print (''.join(c))
	else:
		k = int(i/2)
		if (k%2==0):
			while(j<(b-1)):
				c.append(".")
				j=j+1
			c.append("#")
			print (''.join(c))
		else:
			c.append('#')
			while(j<(b-1)):
				c.append(".")
				j=j+1
			print (''.join(c))
	i=i+1
