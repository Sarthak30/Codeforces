n, s = map(int,raw_input().split())
c = []
flag = 0
cent = []
for i in range(n):
	a, b = map(int,raw_input().split())
	if(a<s or (a==s and b==0)):
		flag = 1
		if b is not 0:
			c.append(100-b)
		else:
			c.append(0)
if(flag == 0):
	print "-1"
else:
	print (max(c))
