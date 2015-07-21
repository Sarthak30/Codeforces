k = int(raw_input())
n = int(raw_input())
i = 1
j = 1
t = 0
m = 0
while t<(n**0.5):
	c = k**i
	t = t+1
	if(c<n):
		j = i
		i = i*2
	elif(c==n):
		print "YES"
		print i-1
		exit()
	elif(c>n):
		i = (i+j)/2
print "NO"
		
