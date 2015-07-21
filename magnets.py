a = int(raw_input())
s = 0
j = 0
for i in range(0,a):
	b = int(raw_input())
	if(j!=b):
		s = s+1
		j=b
	else:
		j=b
print s
