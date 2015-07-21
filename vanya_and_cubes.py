a = int(raw_input())
i = 0
s=0
b = []
while(i<=a):
	b.append(i)
	s = s+sum(b)
	if(s>a):
		print i-1
		break
	elif(s==a):
		print i
		break
	i=i+1
