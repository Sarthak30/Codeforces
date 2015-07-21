a =str(raw_input())
b =str(raw_input())
c=''
for i in range(0,len(a)):
	if(a[i]==b[i]):
		c = c+'0'
	else:
		c = c+'1'
print c

